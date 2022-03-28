
import Divisible


def test_divisible_5():
    x = 18
    res = Divisible.divisible_5(x)
    assert res == True


def test_divisible_7():
    x = 18
    res = Divisible.divisible_7(x)
    assert res == True


def test_divisible_9():
    x = 17
    res = Divisible.divisible_9(x)
    assert res == True


def test_divisible_10():
    x = 15
    res = Divisible.divisible_10(x)
    assert res == True