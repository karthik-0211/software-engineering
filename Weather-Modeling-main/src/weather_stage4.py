"""Stage 4: read multiple sets of inputs from a CSV file.

CSV format: header with at least columns 'a','b','c'.
Example:
a,b,c
0.01,-0.5,10
-0.02,1.0,5
"""
import csv
import sys
from typing import List, Tuple
from src.quadratic import quadratic_value, quadratic_roots


def read_models_csv(path: str) -> List[Tuple[float, float, float]]:
    rows = []
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if reader.fieldnames is None:
            raise ValueError('CSV has no header')
        # normalize fieldnames
        fn = [h.strip().lower() for h in reader.fieldnames]
        for line_no, r in enumerate(reader, start=2):
            try:
                a = float(r.get('a', r.get('A')))
                b = float(r.get('b', r.get('B')))
                c = float(r.get('c', r.get('C')))
            except Exception as exc:
                raise ValueError(f"Failed parsing CSV at line {line_no}: {exc}")
            rows.append((a, b, c))
    return rows


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: weather_stage4.py <csv_file>")
        sys.exit(1)
    models = read_models_csv(sys.argv[1])
    t_default = [0, 5, 10, 15, 20]
    for i, (a, b, c) in enumerate(models, start=1):
        print(f"Model #{i}: a={a}, b={b}, c={c}")
        roots = quadratic_roots(a, b, c)
        print("  Roots:", roots)
        for t in t_default:
            print(f"  t={t} -> y={quadratic_value(a,b,c,t):.4f}")
        print()


if __name__ == '__main__':
    main()
