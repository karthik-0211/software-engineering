"""Stage 3: read a single set of inputs from a plain text file.

Expected file format (plain text):
Line 1: a b c   (space or comma separated)
Optional Line 2: t1 t2 t3 ... (space or comma separated t values)
"""
import sys
from typing import List
from src.quadratic import quadratic_value, quadratic_roots


def read_single_model(path: str):
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    if not lines:
        raise ValueError("Empty input file")
    # parse first line for a b c
    parts = lines[0].replace(',', ' ').split()
    if len(parts) < 3:
        raise ValueError("First line must contain a b c")
    a, b, c = [float(x) for x in parts[:3]]
    if len(lines) > 1:
        t_parts = lines[1].replace(',', ' ').split()
        t_values = [float(x) for x in t_parts]
    else:
        t_values = [0, 5, 10, 15, 20]
    return a, b, c, t_values


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: weather_stage3.py <input_file>")
        sys.exit(1)
    path = sys.argv[1]
    a, b, c, t_values = read_single_model(path)
    print(f"Model: y(t) = {a} t^2 + {b} t + {c}")
    print("Roots:", quadratic_roots(a, b, c))
    for t in t_values:
        print(f"t={t} -> y={quadratic_value(a,b,c,t):.4f}")


if __name__ == '__main__':
    main()
