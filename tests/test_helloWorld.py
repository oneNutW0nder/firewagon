import requests


def test_helloWorld():
    response = requests.get("http://localhost:8080")

    assert "Hello World -- pytesting" in response.text
