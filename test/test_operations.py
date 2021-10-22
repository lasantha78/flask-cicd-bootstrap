import pytest

from service.operations import mysum
def test_sum():
    assert mysum(-1, 1) == 0
    assert mysum(2, 3) == 5
    assert mysum(-1, -2) == -3
    assert mysum(0, -2) == -2