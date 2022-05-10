fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with keyword arguments.
def f(a, b):
    yield a
    yield b

g = f(b=1, a=2)
assert next(g) == 2
assert next(g) == 1

# Test that a generator function can be called with keyword arguments
# and a variable number of arguments.
def f(a, b, *args):
    yield a
    yield b
    yield args

g = f(b=1, a=2, c=3, d=4)
assert next(g) == 2
assert next(g) == 1
assert next(g) == (3, 4)

# Test that a generator function can be called with keyword arguments
# and a variable number of keyword arguments.
def f(a, b, **kwargs):
    yield a
    yield b
    yield kwargs

g = f(b=1, a=2, c=3, d=4)
assert next(g) == 2
assert next(g) == 1
assert next(g
