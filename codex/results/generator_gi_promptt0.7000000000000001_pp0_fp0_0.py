gi = (i for i in ())
# Test gi.gi_code.co_flags:
# Verify that generator methods have a flag set, and other methods don't.
import types
def f():
    yield 1
assert f.__code__.co_flags & types.CO_GENERATOR
def f():
    pass
assert not f.__code__.co_flags & types.CO_GENERATOR
def f():
    for i in range(10):
        yield i
assert f.__code__.co_flags & types.CO_GENERATOR
def f():
    if True:
        yield 1
assert f.__code__.co_flags & types.CO_GENERATOR

# Issue #2464
def coro():
    yield
    yield
    yield

c = coro()
c.__name__
c.__name__ = 'coro'
c.__name__

# Issue #3054
def gen():
    yield

g = gen()
g.__name__
g.__name__ = 'gen'
g.__name__

# Issue #5620
def coro():
    yield
