import sqlite3
from fastapi import FastAPI

app = FastAPI()
DB = "tickets.db"


def init_db():
    con = sqlite3.connect(DB)
    con.execute("CREATE TABLE IF NOT EXISTS tickets (id INTEGER PRIMARY KEY, title TEXT, owner TEXT)")
    con.execute("INSERT OR IGNORE INTO tickets VALUES (1, 'Badge perdu', 'alice')")
    con.commit()
    con.close()


@app.get("/tickets")
def search(owner: str):
    init_db()
    con = sqlite3.connect(DB)
    # FAILLE VOLONTAIRE : requête construite par concaténation (injection SQL)
    rows = con.execute(f"SELECT id, title FROM tickets WHERE owner = '{owner}'").fetchall()
    con.close()
    return [{"id": r[0], "title": r[1]} for r in rows]


def remise(montant: float, vip: bool) -> float:
    if vip:
        return montant * 0.8
    return montant


def tva(montant: float, taux: float = 0.2) -> float:
    if taux < 0:
        raise ValueError("taux négatif")
    if taux > 1:
        raise ValueError("taux supérieur à 100 %")
    return round(montant * (1 + taux), 2)
