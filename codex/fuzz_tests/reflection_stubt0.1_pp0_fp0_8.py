fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with keyword arguments
def gfn(a, b, c):
    yield a
    yield b
    yield c

assert list(gfn(1, 2, 3)) == [1, 2, 3]
assert list(gfn(c=3, b=2, a=1)) == [1, 2, 3]

# Test that a generator function can be called with keyword arguments
# and a default value
def gfn(a, b, c=3):
    yield a
    yield b
    yield c

assert list(gfn(1, 2)) == [1, 2, 3]
assert list(gfn(1, 2, c=4)) == [1, 2, 4]
assert list(gfn(1, 2, 4)) == [1, 2, 4]

# Test that a generator function can be called with keyword arguments
# and a default value
def gfn(a, b=2, c=3):
    yield a
    yield b
    yield c

assert list(gfn(
