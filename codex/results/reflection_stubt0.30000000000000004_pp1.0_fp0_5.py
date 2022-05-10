fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with a keyword argument
def f(a, b=1):
    yield a
    yield b

g = f(1, b=2)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with a keyword argument
def f(a, b=1):
    yield a
    yield b

g = f(1, b=2)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with a keyword argument
def f(a, b=1):
    yield a
    yield b

g = f(1, b=2)
assert next(g) == 1
assert next(g) == 2

# Test that a generator function can be called with a keyword argument
def f(a, b=1):
    yield a
    yield b

g = f(1, b=2)
assert next(g) == 1
assert next(g) == 2

# Test that a
