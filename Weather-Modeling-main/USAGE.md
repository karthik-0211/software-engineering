Weather Modeling - Usage

This repository now includes simple stage scripts demonstrating a quadratic-based weather-modeling example.

Scripts:
- src/weather_stage1.py  : hard-coded variables demo
- src/weather_stage2.py  : keyboard input (enter a b c and optional t)
- src/weather_stage3.py  : read single model from a plain text file (examples/input_single.txt)
- src/weather_stage4.py  : read multiple models from CSV (examples/input_multiple.csv)

Run examples from the repository root, for example:

python3 src/weather_stage1.py
python3 src/weather_stage2.py
python3 src/weather_stage3.py examples/input_single.txt
python3 src/weather_stage4.py examples/input_multiple.csv

Run tests with pytest:

pytest -q


End of files.
