fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with an argument
def gfn(x):
    yield x

gfn(1).__next__()

# Test that a generator function can be called with a keyword argument
def gfn(x=1):
    yield x

gfn(x=2).__next__()

# Test that a generator function can be called with a keyword argument
# and an argument
def gfn(x, y=1):
    yield x
    yield y

g = gfn(2, y=3)
assert g.__next__() == 2
assert g.__next__() == 3

# Test that a generator function can be called with a keyword argument
# and an argument
def gfn(x, y=1):
    yield x
    yield y

g = gfn(2, 3)
assert g.__next__() == 2
assert g.__next__() == 3

# Test that a generator function can be called with a keyword argument
# and an argument
def gfn(x, y=1):
