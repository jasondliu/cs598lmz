from types import FunctionType
a = (x for x in [1])
b = lambda x: x.upper()


def f(x):
    return x.lower()


def g():
    return 3


assert isinstance(a, GeneratorType)
assert isinstance(b, FunctionType)
assert isinstance(f, FunctionType)
assert isinstance(g, FunctionType)


def is_callable(x):
    return hasattr(x, '__call__')


def test_is_callable():
    assert is_callable(a)
    assert is_callable(b)
    assert is_callable(f)
    assert is_callable(g)
    assert is_callable(g()) is False


def is_generator(x):
    return isinstance(x, GeneratorType)


def test_is_generator():
    assert not is_generator(a)
    assert not is_generator(b)
    assert not is_generator(f)
    assert not is_generator(g)
    assert is_generator(g()) is True


def is_function(x):
