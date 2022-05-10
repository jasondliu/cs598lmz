fn = lambda: None
# Test fn.__code__.co_varnames

def f(x, y):
    def g(z):
        return z + x
    return g

assert f(1, 2).__code__.co_varnames == ('z', 'x')
assert f(1, 2)(3) == 4

# Test fn.__code__.co_flags

def f():
    pass
assert f.__code__.co_flags == 0

def f():
    yield 1
assert f.__code__.co_flags == CO_GENERATOR

def f():
    (a + b for c in d)
assert f.__code__.co_flags == CO_GENERATOR

def f():
    nonlocal x
assert f.__code__.co_flags == CO_NONLOCAL

def f():
    yield 1
    nonlocal x
assert f.__code__.co_flags == CO_GENERATOR | CO_NONLOCAL

def f():
    yield from range(10)
assert f.__code__.co_flags == CO_
