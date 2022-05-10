fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Test that a generator function can be called with keyword arguments.
def genfn(a, b):
    yield a
    yield b
g = genfn(b=2, a=1)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with keyword arguments.
def genfn(a, b):
    yield a
    yield b
g = genfn(b=2, a=1)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with keyword arguments.
def genfn(a, b):
    yield a
    yield b
g = genfn(b=2, a=1)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with keyword arguments.
def genfn(a, b):
    yield a
    yield b
g = genfn(b=2, a=1)
assert next(g) == 1
assert next(g)
