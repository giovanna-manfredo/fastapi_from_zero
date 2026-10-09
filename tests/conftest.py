import pytest
from fastapi.testclient import TestClient

from fastapi_from_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)

from sqlalchemy import create_engine

def session():
    engine = create_engine("sqlite:///:memory:")
     