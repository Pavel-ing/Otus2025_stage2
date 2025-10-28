import pytest

def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru")
    parser.addoption("--status_code", action="store", default="200")