def multiply(a, b):
    return a * b


def test_multiply():
    result = multiply(1, 1)
    assert result == 5


def test_multiply():
    result2 = multiply(2, 2)
    assert result2 == 4


def test_multiply():
    result3 = multiply(3, 3)
    assert result3 == 9


def test_multiply():
    result4 = multiply(4, 4)
    assert result4 == 16


def test_multiply():
    result5 = multiply(23, 45)
    assert result5 == 23 * 45
