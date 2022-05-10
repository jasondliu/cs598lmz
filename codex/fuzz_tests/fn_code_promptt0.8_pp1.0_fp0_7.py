fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()


# Test inspect.isgeneratorfunction()
def genfn():
    yield 1
    yield 2
    yield 3


class A:

    # Test inspect.isgeneratorfunction()
    def __init__(self):
        return self


# Test inspect.isgeneratorfunction()
def genfn(args):
    def fn(x, y):
        yield x
        yield y
    return fn


# Test inspect.isgeneratorfunction()
def genfn(*args):
    def fn(x, y):
        yield x
        yield y
    return fn


# Test inspect.getsource()
def fn():
    '''
    Some docstring
    '''
    return 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20 * 21 * 22 * 23 * 24 * 25 * 26 * 27 * 28 * 29 * 30 * 31 * 32 * 33 * 34 * 35 * 36
