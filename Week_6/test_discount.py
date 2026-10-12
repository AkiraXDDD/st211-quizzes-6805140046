import pytest
from discount import apply_discount

@pytest.mark.parametrize("price, percent, expected", [
    (100,0,100),
    (100,50,50),
    (100,10,90),
    (80,10,72)
])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected

@pytest.mark.parametrize("bad_percent", [-1, -50, 101, 200])
def test_invalid_percent(bad_percent):
    with pytest.raises(ValueError):
        apply_discount(100, bad_percent)

@pytest.mark.parametrize("price, percent, expected", [
    pytest.param(100,0,100, id="no_discount"),
    pytest.param(100,50,50, id="half_price"),
    pytest.param(100,10,90, id="ninety_percent_discount"),
    pytest.param(80,10,72, id="ten_percent_discount")
])
def test_unique_id_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected