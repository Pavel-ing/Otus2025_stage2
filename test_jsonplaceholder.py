import pytest
import requests

JSON_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    response = requests.get(f"{JSON_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert "id" in data[0]
    assert "userId" in data[0]
    assert "title" in data[0]


def test_get_single_post():
    response = requests.get(f"{JSON_URL}/posts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)
    assert isinstance(data["userId"], int)


@pytest.mark.parametrize("post_id", [1, 3, 5, 7, 9])
def test_get_post_by_id(post_id):
    response = requests.get(f"{JSON_URL}/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id


def test_get_users():
    response = requests.get(f"{JSON_URL}/users")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    user = data[0]
    assert "id" in user
    assert "name" in user
    assert "username" in user


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_user_by_id(user_id):
    response = requests.get(f"{JSON_URL}/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
