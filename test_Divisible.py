
import Divisible

import pytest


@pytest.fixture
def input():
    x=18
    return x

def test_divisible_5(input):
    x = 18
    res = Divisible.divisible_5(input)
    assert res == True


def test_divisible_7(input):
    x = 18
    res = Divisible.divisible_7(input)
    assert res == True


def test_divisible_9(input):
    x = 17
    res = Divisible.divisible_9(input)
    assert res == True


def test_divisible_10(input):
    x = 15
    res = Divisible.divisible_10(input)
    assert res == True