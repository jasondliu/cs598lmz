fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with keyword arguments
def f(a, b, c):
    yield a
    yield b
    yield c

g = f(1, 2, 3)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

g = f(c=3, b=2, a=1)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3

# Test that a generator function can be called with keyword arguments
# and a variable number of arguments
def f(a, b, c, *args):
    yield a
    yield b
    yield c
    yield args

g = f(1, 2, 3, 4, 5, 6)
assert next(g) == 1
assert next(g) == 2
assert next(g) == 3
assert next(g) == (4, 5, 6)

g = f(c=3, b=2, a=1, 4, 5, 6)
assert next(g
