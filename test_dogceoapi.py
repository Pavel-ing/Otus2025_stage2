import pytest
import requests

JSON_URL = "https://dog.ceo/api"


def test_list_breeds():
    response = requests.get(f"{JSON_URL}/breeds/list/all")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "message" in data
    assert "terrier" in data["message"]
    assert "bulldog" in data["message"]


@pytest.mark.parametrize("breed", ["malamute", "husky", "retriever"])
def test_list_sub_breeds(breed):
    response = requests.get(f"{JSON_URL}/breed/{breed}/list")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert isinstance(data["message"], list)


def test_get_random_image_from_breed():
    breed = "husky"
    response = requests.get(f"{JSON_URL}/breed/{breed}/images/random")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert breed in data["message"]


@pytest.mark.parametrize("breed,sub_breed", [
    ("mastiff", "bull"),
    ("retriever", "curly"),
    ("terrier", "australian"),
])
def test_get_random_image_from_subbreed(breed, sub_breed):
    response = requests.get(
        f"{JSON_URL}/breed/{breed}/{sub_breed}/images/random")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert breed in data["message"]
    assert sub_breed in data["message"]


def test_subbreeds_for_bulldog():
    response = requests.get(f"{JSON_URL}/breed/bulldog/list")

    data = response.json()
    sub_breeds = data["message"]
    assert len(sub_breeds) > 0
    assert "boston" in sub_breeds
    assert "english" in sub_breeds
    assert "french" in sub_breeds
