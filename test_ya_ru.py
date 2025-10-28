import pytest
import requests


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def status_code(request):
    return int(request.config.getoption("--status_code"))


def test_site_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code,f"ERROR {response.status_code}, CHECK URL: {url}"
