import pytest
import requests
import jsonschema
from datetime import datetime

# Base URL of the API
BASE_URL = "https://jsonplaceholder.typicode.com"

# Example schema for JSON validation
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    },
    "required": ["id", "title", "body", "userId"]
}

# Fixture to add time tracking to each test for reporting
@pytest.fixture
def log_time():
    start_time = datetime.now()
    yield
    print(f"Test duration: {(datetime.now() - start_time).total_seconds()} seconds")

# GET Test
def test_get_posts(log_time):
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "title" in response.json(), "Response missing 'title' field"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"GET Response: {response.json()}")

# POST Test
def test_create_post(log_time):
    payload = {"title": "New Post", "body": "This is a test post", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
    assert response.json()["title"] == "New Post", "Title mismatch"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"POST Response: {response.json()}")

# PUT Test
def test_update_post(log_time):
    payload = {"id": 1, "title": "Updated Post", "body": "Updated content", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["title"] == "Updated Post", "Title not updated"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"PUT Response: {response.json()}")

# DELETE Test
def test_delete_post(log_time):
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json() == {}, "Expected empty response"
    print("DELETE successful")

# Authentication test (simulated example)
def test_authentication_failure(log_time):
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/posts/1", headers=headers)
    assert response.status_code == 200, "This API doesn't require auth, but should fail with real auth"
    print(f"Auth Response: {response.status_code}")