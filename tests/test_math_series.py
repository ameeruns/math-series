from math_series import __version__ 
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == "0.1.0"
def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 0
    assert actual == expected
def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 1
    assert actual == expected
def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected
def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 3
    assert actual == expected
def test_fibonacci_six():
    actual = fibonacci(6)
    expected = 5
    assert actual == expected

#Lucas Tests
def test_lucas_one():
    actual = lucas(1)
    expected = 2
    assert actual == expected
def test_lucas_two():
    actual = lucas(2)
    expected = 1
    assert actual == expected
def test_lucas_three():
    actual = lucas(3)
    expected = 3
    assert actual == expected
def test_lucas_four():
    actual = lucas(4)
    expected = 4
    assert actual == expected
def test_lucas_five():
    actual = lucas(5)
    expected = 7
    assert actual == expected
def test_lucas_six():
    actual = lucas(6)
    expected = 11
    assert actual == expected

#Sum series tests
def test_sumseries_fib_one():
    actual = sum_series(1)
    expected = 0
    assert actual == expected
def test_sumseries_fib_one1():
    actual = sum_series(1,0,1)
    expected = 0
    assert actual == expected
def test_sumseries_fib_two1():
    actual = sum_series(2,0,1)
    expected = 1
    assert actual == expected
def test_sumseries_fib_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected
def test_sumseries_fib_three():
    actual = sum_series(3)
    expected = 1
    assert actual == expected
def test_sumseries_fib_four():
    actual = sum_series(4)
    expected = 2
    assert actual == expected
def test_sumseries_lucas_one():
    actual = sum_series(1,2,1)
    expected = 2
    assert actual == expected
def test_sumseries_lucas_one1():
    actual = sum_series(1,2,1)
    expected = 2
    assert actual == expected
def test_sumseries_lucas_two():
    actual = sum_series(2,2,1)
    expected = 1
    assert actual == expected
def test_sumseries_lucas_three():
    actual = sum_series(3,2,1)
    expected = 3
    assert actual == expected
def test_sumseries_lucas_four():
    actual = sum_series(4,2,1)
    expected = 4
    assert actual == expected