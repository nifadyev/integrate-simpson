"""Integrate function using Simpson method from `scipy`."""

from itertools import islice

from scipy.integrate import simps
import numpy as np
import click


def function(x: float) -> float:
    """Find function's result with specified argument.

    Args:
        x: float or int value.

    Returns:
        float

    """
    return (x**2 + 3 * x) / (x + 1) + np.cos(x)


def calculate_max_forth_derivative(low: float, high: float) -> float:
    """Calculate forth derivative of specified function.

    Set high argument instead of `x` in numerator and
    low argument instead of `x` in denominator.

    Args:
        low: left range boundary.
        high: right range boundary.

    Returns:
        float: max value of forth derivative.

    """
    return (24 * high * (high + 3)) / (low + 1)**5\
        + np.cos(high)\
        + 24 / (low + 1)**3\
        - (24 * (2*high + 3)) / (low + 1)**4


def calculate_integration_error(
        max_forth_derivative: float, low: float, high: float, length: int) -> float:
    """Find integration error if Simpson method is used.

    Args:
        max_forth_derivative: precalculated value.
        low: left range boundary.
        high: right range boundary.
        length: number of values in range.
    Returns:
        float: approximate integration error.

    """
    step = (high - low) / length

    return (step)**4 / 180 * max_forth_derivative * (high - low)


def express_step_from_error(
        error: float, max_forth_derivative: float, low: float, high: float) -> float:
    """Get step from known integration error using it's formula.

    Args:
        error: precalculated integration error.
        max_forth_derivative: precalculated value.
        high: right range boundary.
        length: number of values in range.

    Returns:
        float: distance between values in range.

    """
    return ((error) / 180 * max_forth_derivative * (high - low))**0.25 * 20


@click.command()
@click.option('--range_start', type=float, default=0.0, help='Left range boundary')
@click.option('--range_end', type=float, default=1.0, help='Right range boundary')
@click.option('--range_length', type=int, default=10, help='Number of values in range')
def main(range_start: float, range_end: float, range_length: int) -> None:
    """Integrate function using Simpson method.

    Range is set by user or default range is used.
    """
    values = np.linspace(range_start, range_end, range_length)
    result = simps(function(values), values)
    max_forth_derivative = calculate_max_forth_derivative(range_start, range_end)
    error = calculate_integration_error(max_forth_derivative, range_start, range_end, range_length)
    step = express_step_from_error(error, max_forth_derivative, range_start, range_end)

    first_values = ', '.join(f'{value:5.5f}' for value in islice(values, 10))
    first_values_length = 10 if len(values) > 10 else len(values)

    print('Function: (x^2 + 3 * x) / (x + 1) + cos(x), '
          f'interval: [{range_start}, {range_end}]\n')
    print(f'First {first_values_length} values: {first_values}\n')
    print(f'Result of integration using Simpson method: {result}')
    print(f'Integration error: {error}')
    print(f'Step (based on integration error): {step}')


if __name__ == '__main__':
    main()
