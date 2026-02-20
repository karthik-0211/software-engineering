"""Stage 2: keyboard input for a single model."""
import sys
from typing import List
from src.quadratic import quadratic_value, quadratic_roots


def parse_floats_from_prompt(prompt: str, expected: int) -> List[float]:
    s = input(prompt).strip()
    parts = s.replace(',', ' ').split()
    if len(parts) < expected:
        raise ValueError(f"Expected at least {expected} values, got {len(parts)}")
    return [float(x) for x in parts[:expected]]


def main() -> None:
    try:
        a, b, c = parse_floats_from_prompt("Enter a b c (space separated): ", 3)
        t_in = input("Enter t (single) or leave blank to use default times: ").strip()
        t_values = [float(t_in)] if t_in else [0, 5, 10, 15, 20]
        roots = quadratic_roots(a, b, c)
        print("Roots:", roots)
        for t in t_values:
            print(f"t={t} -> y={quadratic_value(a,b,c,t):.4f}")
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
