from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_from_zero.app import app


def test_root_should_return_ok_and_hello_world():
    client = TestClient(app) # arrange

    response = client.get("/") # act

    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {"message": "Hello World!"} # assert
