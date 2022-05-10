fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
# Test fn.__code__.co_names
# Test fn.__code__.co_nlocals


def test_extended_argument_syntax():
    from __pypy__ import extended_arg
    def f():
        pass
    assert f.__code__.co_flags & extended_arg

    def f(a, *b, **c):
        pass
    assert f.__code__.co_flags & extended_arg

    def f(a, b=10, c=20, *d, **e):
        pass
    assert f.__code__.co_flags & extended_arg

def test_kwargs_and_extended_arg():
    # CPython doesn't like a function with **kwargs but also with
    # extended arg syntax
    def f(a, **kwargs):
        pass
    def g(a, *args):
        pass
    def h(a, *args, **kwargs):
        pass
    py.test.ra
