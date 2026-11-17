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

import pytest
from app.main import tva


def test_tva():
    assert tva(100) == 120.0


def test_tva_invalide():
    with pytest.raises(ValueError):
        tva(100, -1)
    with pytest.raises(ValueError):
        tva(100, 2)
