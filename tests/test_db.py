from fastapi_from_zero.models import User


def test_create_user():
    user = User(username="test", email="teste@test.com", password="secret")

    assert user.username == "test"
