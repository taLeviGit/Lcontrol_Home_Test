import pytest
import requests
import jsonschema
from datetime import datetime

# בסיס ה-URL של ה-API
BASE_URL = "https://jsonplaceholder.typicode.com"

# סכמה לדוגמה לבדיקת JSON
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

# פיקסטורה להוספת זמן לכל בדיקה לדוח
@pytest.fixture
def log_time():
    start_time = datetime.now()
    yield
    print(f"Test duration: {(datetime.now() - start_time).total_seconds()} seconds")

# 1. בדיקת GET
def test_get_posts(log_time):
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "title" in response.json(), "Response missing 'title' field"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"GET Response: {response.json()}")

# 2. בדיקת POST
def test_create_post(log_time):
    payload = {"title": "New Post", "body": "This is a test post", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, f"Expected status 201, got {response.status_code}"
    assert response.json()["title"] == "New Post", "Title mismatch"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"POST Response: {response.json()}")

# 3. בדיקת PUT
def test_update_post(log_time):
    payload = {"id": 1, "title": "Updated Post", "body": "Updated content", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["title"] == "Updated Post", "Title not updated"
    jsonschema.validate(instance=response.json(), schema=POST_SCHEMA)
    print(f"PUT Response: {response.json()}")

# 4. בדיקת DELETE
def test_delete_post(log_time):
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json() == {}, "Expected empty response"
    print("DELETE successful")

# 5. בדיקת אימות (דוגמה מדומה)
def test_authentication_failure(log_time):
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/posts/1", headers=headers)
    assert response.status_code == 200, "This API doesn't require auth, but should fail with real auth"
    print(f"Auth Response: {response.status_code}")