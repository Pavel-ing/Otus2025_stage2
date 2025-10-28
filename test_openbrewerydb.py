import pytest
import requests

JSON_URL = "https://api.openbrewerydb.org/v1/breweries"


def test_get_breweries():
    response = requests.get(JSON_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    brewery = data[0]
    assert "id" in brewery
    assert "name" in brewery


@pytest.mark.parametrize("search", ["brew", "beer", "ale"])
def test_search_by_different_terms(search):
    response = requests.get(f"{JSON_URL}?by_name={search}")
    assert response.status_code == 200


def test_filter_by_city():
    response = requests.get(f"{JSON_URL}?by_city=san_diego")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert "city" in data[0]


def test_get_invalid_brewery():
    response = requests.get(f"{JSON_URL}/invalid_id")
    assert response.status_code == 404


@pytest.mark.parametrize("state", ["texas", "new_york", "oregon"])
def test_state_filter(state):
    response = requests.get(f"{JSON_URL}?by_state={state}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
