"""Integrate function using Simpson method from `scipy`."""

from itertools import islice

from scipy.integrate import simps 
import numpy as np
import click


def function(x):
    """Find function's result with specified argument.

    Args:
        x: float or int value.

    Returns:
        float
    """
    return (x**3 + np.sin(x/4)) / (x**2 + x + 10)


@click.command()
@click.option(
    '--range_start', type=float, default=0.0, help='Left range boundary')
@click.option(
    '--range_end', type=float, default=1.0, help='Right range boundary')
@click.option(
    '--range_length', type=int, default=10, help='Number of values in range')
def main(range_start, range_end, range_length):
    """Integrate function using Simpson method.

    Range is set by user or default range is used.
    """
    values = np.linspace(range_start, range_end, range_length)
    first_values = ", ".join(f'{value:5.5f}' for value in islice(values, 10))
    first_values_length = 10 if len(values) > 10 else len(values)
    result = simps(function(values), values)

    print('Function: (x^3 + sin(x/4)) / (x^2 + x + 10), '
          f'interval: [{range_start}, {range_end}]\n')
    print(f'First {first_values_length} values: {first_values}\n')
    print(f'Result of integration using Simpson method: {result}')


if __name__ == '__main__':
    main()
