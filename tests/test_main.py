from fastapi.testclient import TestClient
from app.main import app, remise

client = TestClient(app)


def test_search():
    r = client.get("/tickets", params={"owner": "alice"})
    assert r.status_code == 200


def test_remise_vip():
    assert remise(100, True) == 80


def test_remise_non_vip():
    assert remise(100, False) == 100
