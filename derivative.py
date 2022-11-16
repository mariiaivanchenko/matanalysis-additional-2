def single_derivative(func: str) -> str:
    """
    Computes derivative of a single function.
    Some examples:
    >>> single_derivative("sin(5x)")
    '5*cos(5x)'
    >>> single_derivative("cos(3x)")
    '-3*sin(3x)'
    >>> single_derivative("e^(-2x)")
    '-2*e^(-2x)'
    >>> single_derivative("x^(3)")
    '3*x^(2)'
    >>> single_derivative("121")
    '0'
    """
    if func.isnumeric():
        return '0'

    


def combine_multipliers(der, others):
    """
    :param der: already found derivative of a single function
    :param others: other functions-multipliers
    :return: result of single chain rule
    >>> found_derivative = "2"
    >>> other = ["x^(2)", "sin(1x)"]
    >>> combine_multipliers(found_derivative, other)
    '2*x^(2)*sin(1x)'
    >>> found_derivative = "2"
    >>> other = []
    >>> combine_multipliers(found_derivative, other)
    '2'
    """
    return "*".join([der] + others)


def derivative_of_product(some_funcs: list) -> str:
    """
    Using the chain rule finds a derivative of a product
    example of input: ["-1", "e^(5x)", "cos(-2x)"]
    approximate output: 5*e^(5x)*-1*cos(-2x) + 2*sin(-2x)*-1*e^(5x)
    :param some_funcs: list of functions.
    """
    res = []
    # chain rule
    for ind, func in enumerate(some_funcs):
        others = some_funcs[:ind] + some_funcs[ind + 1:]
        der = single_derivative(func)
        adder = combine_multipliers(der, others)
        res.append(adder)
    return " + ".join(res)


def find_derivative(equation: str) -> str:
    """
    Main function. Receives the sum of functions as a string
    :param equation: str representation of the function.

    Examples: '2*cos(1x)*x^(1) + x^(1)*e^(2x)', or '2*x^(3) + -5*sin(-3x)', or '-4*x^(5)*cos(-1x) + -4'
    There will not be no inputs like '-sin(1x)', or '-e^(3x)', or '-x^(2)'.
    Instead the minus will be converted to '-1':  '-1*sin(1x)' ...

    :return: returns the derivative of the sum of functions.
    """
    parts = equation.split(" + ")

    separately_computed = []
    for part in parts:
        multipliers = part.split("*")
        separately_computed.append(derivative_of_product(multipliers))

    return " + ".join(separately_computed)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())