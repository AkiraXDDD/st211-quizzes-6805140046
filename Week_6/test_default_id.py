import pytest

@pytest.mark.parametrize("user", [
    {"name": "Mark", "age": 20},
    {"name": "Sarah", "age": 19}
])
def test_user_has_name(user):
    assert "name" in user

@pytest.mark.parametrize("user", [
    {"name": "Mark", "age": 20},
    {"name": "Sarah", "age": 19}
], ids=["Mark-adult", "Sarah-adult"])
def test_unique_id(user):
    assert "name" in user