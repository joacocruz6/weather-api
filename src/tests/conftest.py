import pytest
from unittest import mock

@pytest.fixture
def ok_response():
    yield 200

@pytest.fixture
def bad_request():
    yield 400

@pytest.fixture
def server_error():
    yield 500

@pytest.fixture
def api_key():
    yield "some_false_api_key"

@pytest.fixture
def get_mock_response():
    data = {}
    yield data
