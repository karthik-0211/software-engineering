"""Quadratic utilities for weather-modeling stages.

Provides quadratic_value(a,b,c,t) and quadratic_roots(a,b,c).
"""
from typing import Tuple, Optional
import math


def quadratic_value(a: float, b: float, c: float, t: float) -> float:
    """Return y(t) = a*t^2 + b*t + c."""
    return a * t * t + b * t + c


def quadratic_roots(a: float, b: float, c: float) -> Tuple[Optional[float], Optional[float]]:
    """Return the real roots of ax^2 + bx + c = 0.

    Returns a tuple (r1, r2) where each is a float or None if not present.
    If a == 0 and b != 0, returns (x, None) for the linear solution.
    If both a and b are zero, returns (None, None).
    If the discriminant is negative, returns (None, None).
    """
    # Handle linear and degenerate cases
    if a == 0.0:
        if b == 0.0:
            return (None, None)
        return (-c / b, None)

    disc = b * b - 4.0 * a * c
    if disc < 0.0:
        return (None, None)
    sqrt_d = math.sqrt(disc)
    r1 = (-b + sqrt_d) / (2.0 * a)
    r2 = (-b - sqrt_d) / (2.0 * a)
    return (r1, r2)


if __name__ == '__main__':
    # quick demo
    a, b, c = 0.01, -0.5, 10.0
    print(f"Model: y(t) = {a} t^2 + {b} t + {c}")
    print("Roots:", quadratic_roots(a, b, c))
    for t in [0, 5, 10, 15, 20]:
        print(f"t={t:>3} -> y={quadratic_value(a,b,c,t):.4f}")
