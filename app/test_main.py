from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to Task Tracker API"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_list_task():
    response = client.post("/tasks", json={"title": "Learn DevOps"})
    assert response.status_code == 201
    assert response.json()["title"] == "Learn DevOps"

    response = client.get("/tasks")
    titles = [t["title"] for t in response.json()]
    assert "Learn DevOps" in titles


def test_delete_missing_task_returns_404():
    response = client.delete("/tasks/9999")
    assert response.status_code == 404