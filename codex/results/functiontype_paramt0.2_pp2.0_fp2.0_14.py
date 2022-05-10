from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# doctest: +ELLIPSIS
# doctest: +NORMALIZE_WHITESPACE
def f(x):
    """
    >>> f(1)
    1
    >>> f(2)
    2
    """
    return x

list(FunctionType(f.__code__, globals(), 'f'))

# doctest: +ELLIPSIS
# doctest: +NORMALIZE_WHITESPACE
def f(x):
    """
    >>> f(1)
    1
    >>> f(2)
    2
    """
    return x

list(FunctionType(f.__code__, globals(), 'f'))

# doctest: +ELLIPSIS
# doctest: +NORMALIZE_WHITESPACE
def f(x):
    """
    >>> f(1)
    1
    >>> f(2)
    2
    """
    return x

list(FunctionType(f.__code__, globals(), 'f'))
