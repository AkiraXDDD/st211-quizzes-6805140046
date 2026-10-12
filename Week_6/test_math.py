import pytest
from math_utils import is_even, factorial

@pytest.mark.parametrize("number", [2,4,8,6])
def test_even_true(number):
    assert is_even(number) is True

@pytest.mark.parametrize("n, expected", [
    (1,1),
    (2,2),
    (3,6),
    (4,24)
])
def test_factorial(n, expected):
    assert factorial(n) == expected
