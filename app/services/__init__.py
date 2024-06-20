# tests/test_user.py
import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "test", "password": "test"})
    assert response.status_code == 200
    assert response.json()["username"] == "test"
