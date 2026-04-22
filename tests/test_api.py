import pytest
from clients.api_client import APIClient
from utils.data_loader import load_json
from jsonschema import validate
from schemas.post_schema import post_schema

client = APIClient()

# Load test data
test_data = load_json("data/user_data.json")

# ------------------ GET ------------------
def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200

# ------------------ POST (Data Driven) ------------------
@pytest.mark.parametrize("payload", test_data)
def test_create_post(payload):
    response = client.post("/posts", payload)

    assert response.status_code == 201
    response_json = response.json()

    assert response_json["title"] == payload["title"]

    validate(instance=response_json, schema=post_schema)

# ------------------ PUT ------------------
def test_update_post():
    payload = {
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = client.put("/posts/1", payload)

    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"

# ------------------ DELETE ------------------
def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200