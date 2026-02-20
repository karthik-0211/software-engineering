"""Stage 1: hard-coded variables example."""
from src.quadratic import quadratic_value, quadratic_roots


def main() -> None:
    a, b, c = 0.01, -0.5, 10.0   # hard-coded model coefficients
    t_values = [0, 5, 10, 15, 20]

    print(f"Model: y(t) = {a} t^2 + {b} t + {c}")
    roots = quadratic_roots(a, b, c)
    print("Roots:", roots)
    for t in t_values:
        print(f"t={t:>3} -> y={quadratic_value(a,b,c,t):.4f}")


if __name__ == '__main__':
    main()
