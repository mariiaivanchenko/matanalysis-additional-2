def evaluate_at_point(function: str, point: float) -> float:
    """
    Evaluates a function at a certain point.
    :param function: same requirements as in the previous task.
    :param point: some value of x
    :return: value of the function when x == point
    """
    pass

def newtons_method(func: str, a: float, b: float, start: float, epsilon: float) -> float:
    """
    Finds the solution of the equation (x value) 'func = 0' on the interval [a, b].
    Start with 'start' and stops when |func(x_i)| < epsilon

    Example of input: newtons_method(func="x^(2) + -4", a=1, b=3, start=1.5, epsilon=0.000001).
    Should return approximately 2.

    :param func: a string representation of a function
    :param a: start of the interval
    :param b: end of the interval
    :param start: x_0
    :param epsilon: accuracy of the final point
    :return: point at x-axis
    """
    pass