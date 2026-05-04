import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/api/v1/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()