import pytest

def division(a, b):
    return a / b

def test_division():
    assert division(4, 2) == 2
    assert division(0, 1) == 0

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)

