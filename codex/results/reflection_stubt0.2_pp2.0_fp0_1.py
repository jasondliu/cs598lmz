fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with keyword arguments
def g(x, y=1):
    yield x
    yield y

g(1)
g(1, 2)
g(y=2, x=1)

# Test that a generator function can be called with a keyword argument
# that is a generator expression
def g(x, y=1):
    yield x
    yield y

g(1, y=(i for i in ()))

# Test that a generator function can be called with a keyword argument
# that is a generator expression
def g(x, y=1):
    yield x
    yield y

g(1, y=(i for i in ()))

# Test that a generator function can be called with a keyword argument
# that is a generator expression
def g(x, y=1):
    yield x
    yield y

g(1, y=(i for i in ()))

# Test that a generator function can be called with a keyword argument
# that is a generator expression
def g(x, y=1):
