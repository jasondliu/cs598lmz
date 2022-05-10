fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with an arbitrary number of
# arguments.
def gfn(*args):
    yield args

g = gfn(1, 2, 3)
assert next(g) == (1, 2, 3)

# Test that a generator function can be called with keyword arguments.
def gfn(**kwargs):
    yield kwargs

g = gfn(a=1, b=2)
assert next(g) == {'a': 1, 'b': 2}

# Test that a generator function can be called with both positional and
# keyword arguments.
def gfn(*args, **kwargs):
    yield args, kwargs

g = gfn(1, 2, 3, a=4, b=5)
assert next(g) == ((1, 2, 3), {'a': 4, 'b': 5})

# Test that a generator function can be called with both positional and
# keyword arguments.
def gfn(a, b, *args, **kwargs):
    yield a, b, args
