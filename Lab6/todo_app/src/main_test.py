from fastapi import FastAPI, Body
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_first_func():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World"}


def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}

def test_read_item_with_query_params():
    response = client.get("/items/?skip=2&limit=5")
    assert response.status_code == 200
    assert response.json() == {"skip": 2, "limit": 5}

def test_read_item_details():
    response = client.get("/items/42/details?q=search_query")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "search_query"}

def test_create_item():
    item_data = {"name": "New Item", "description": "A new item"}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json() == item_data

def test_update_item():
    item_data = {"name": "Updated Item", "description": "An updated item"}
    response = client.put("/items/42", json=item_data)
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "updated_item": item_data}

def test_delete_item():
    response = client.delete("/items/42")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 42 deleted"}