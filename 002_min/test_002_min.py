import run_002_min


def test_empty_list():
    assert run_002_min.get_min([]) == 0


def test_0():
    assert run_002_min.get_min([0]) == 0


def test_single_positive():
    assert run_002_min.get_min([1]) == 1


def test_single_negative():
    assert run_002_min.get_min([-1]) == -1


def test_multiple_positive():
    assert run_002_min.get_min([1, 2, 3]) == 1


def test_multiple_negative():
    assert run_002_min.get_min([-1, -2, -3]) == -3


def test_multiple_mixed():
    assert run_002_min.get_min([-1, 2, -3]) == -3


def test_multiple_zero_sum():
    assert run_002_min.get_min([-1, -2, 1, 2]) == -2


def test_multiple_float():
    assert run_002_min.get_min([1.5, 2.5, 3.5]) == 1.5


def test_mixed_float_int():
    assert run_002_min.get_min([1.5, 2.5, 3.5, 3]) == 1.5
