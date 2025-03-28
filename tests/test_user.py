import pytest
import requests

def test_users_endpoint_unauthorized(mocker):
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Mock the server response
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 401
    mock_get.return_value.text = ""

    # Make a GET request
    response = requests.get(url, params=params)

    # Assert the HTTP status code is 401
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got {response.text}"

def test_users_endpoint_authorized(mocker):
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Mock the server response
    mock_get = mocker.patch("requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = ""

    # Make a GET request
    response = requests.get(url, params=params)

    # Assert the HTTP status code is 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got {response.text}"
