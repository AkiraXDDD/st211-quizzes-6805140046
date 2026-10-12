import pytest

@pytest.mark.parametrize("x, y, z", [
    (2,2,4),
    (3,3,27),
    pytest.param(5,2,20, mark = pytest.mark.xfail(reason="known bug"))
])
def test_exponent(x,y,z):
    assert x ** y == z