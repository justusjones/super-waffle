import run_001_sum


def test_empty_list():
    assert run_001_sum.calculate_sum([]) == 0


def test_0():
    assert run_001_sum.calculate_sum([0]) == 0


def test_single_positive():
    assert run_001_sum.calculate_sum([1]) == 1


def test_single_negative():
    assert run_001_sum.calculate_sum([-1]) == -1


def test_multiple_positive():
    assert run_001_sum.calculate_sum([1, 2, 3]) == 6


def test_multiple_negative():
    assert run_001_sum.calculate_sum([-1, -2, -3]) == -6


def test_multiple_mixed():
    assert run_001_sum.calculate_sum([-1, 2, -3]) == -2


def test_multiple_zero_sum():
    assert run_001_sum.calculate_sum([-1, -2, 1, 2]) == 0


def test_multiple_float():
    assert run_001_sum.calculate_sum([1.5, 2.5, 3.5]) == 7.5


def test_mixed_float_int():
    assert run_001_sum.calculate_sum([1.5, 2.5, 3.5, 3]) == 10.5
