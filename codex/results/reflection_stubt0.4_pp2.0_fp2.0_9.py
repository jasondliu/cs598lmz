fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

try:
    fn()
except TypeError:
    pass
else:
    raise Exception("Expected TypeError")

# Test that we don't crash when calling a generator that has been closed
# and had its gi_frame set to NULL.

def gen():
    yield 1

g = gen()
next(g)
g.close()
g.gi_frame = None

try:
    next(g)
except StopIteration:
    pass
else:
    raise Exception("Expected StopIteration")

# Test that we don't crash when calling a generator that has been closed
# and had its gi_frame set to NULL.

def gen():
    yield 1

g = gen()
next(g)
g.close()
g.gi_frame = None

try:
    next(g)
except StopIteration:
    pass
else:
    raise Exception("Expected StopIteration")

# Test that we don't crash when calling a generator that has been closed
# and had its gi_frame set to
