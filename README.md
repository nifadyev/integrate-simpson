# Integrate Simpson

![](https://img.shields.io/badge/python-v3.8-blue) ![](https://img.shields.io/badge/numpy-1.17.4-blue) ![](https://img.shields.io/badge/scipy-1.3.2-blue) ![](https://img.shields.io/badge/platform-windows%20%7C%20linux-lightgrey) ![](https://img.shields.io/badge/license-MIT-green)

Tool for integrating function using Simpson method.

## Requirements
- python3.8+
- pip
- virtualenv (optional)

### Pip packages
Install required packages using `virtualenv`

```bash
python -m virtualenv env && source env/bin/activate
python -m pip install -r requirements.txt
```

## Usage

The set of available options are:

 * `--range_start`: left range boundary, default=0.0, example: -2.5
 * `--range_end`: right range boundary, default=1.0, example: 15.0
 * `--range_length`: number of values in range, default=10, example: 50

## Example

Use default range [0.0, 1.0] with 30 values

`python main.py --range_length 30`

### Output

Output contains:
 * function
 * first 10 values
 * result of integration

```bash
Function: (x^3 + sin(x/4)) / (x^2 + x + 10), interval: [0.0, 1.0]

First 10 values: 0.00000, 0.03448, 0.06897, 0.10345, 0.13793, 0.17241, 0.20690, 0.24138, 0.27586, 0.31034

Result of integration using Simpson method: 0.03299210268431508
```
