import math
from src.quadratic import quadratic_value, quadratic_roots


def is_close(a, b, tol=1e-9):
    if a is None or b is None:
        return False
    return abs(a - b) <= tol


def test_quadratic_value():
    assert math.isclose(quadratic_value(1, 0, 0, 2), 4.0)


def test_quadratic_roots_two_real():
    r1, r2 = quadratic_roots(1, -3, 2)  # roots 1 and 2
    assert {round(r1, 6), round(r2, 6)} == {1.0, 2.0}


def test_quadratic_roots_linear():
    r1, r2 = quadratic_roots(0.0, 2.0, -4.0)  # 2x -4 =0 -> x=2
    assert math.isclose(r1, 2.0)
    assert r2 is None


def test_quadratic_roots_complex():
    r1, r2 = quadratic_roots(1.0, 0.0, 1.0)
    assert r1 is None and r2 is None
