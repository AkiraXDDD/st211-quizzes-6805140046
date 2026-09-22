import pytest
import sys

@pytest.mark.skip(reason="feature not implemented yet")
def test_future_feature():
    assert False

@pytest.mark.skipif(sys.version_info < (3,8), reason = "requires python 3.8+")
def test_require():
    assert True