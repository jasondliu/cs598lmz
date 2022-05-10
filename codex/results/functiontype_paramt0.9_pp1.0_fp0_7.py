from types import FunctionType
list(FunctionType(None, None, None, [yield_, 1, 2, 3]))


if __name__ == "__main__":
    import sys
    import doctest
    doctest.testmod(sys.modules[__name__])
