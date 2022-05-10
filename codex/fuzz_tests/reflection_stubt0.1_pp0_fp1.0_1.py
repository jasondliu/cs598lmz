fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with a keyword argument
def g():
    yield
g.__code__ = gi
g(x=1)

# Test that a generator function can be called with a keyword argument
# and a positional argument
def g():
    yield
g.__code__ = gi
g(1, x=1)

# Test that a generator function can be called with a keyword argument
# and a positional argument
def g():
    yield
g.__code__ = gi
g(1, x=1)

# Test that a generator function can be called with a keyword argument
# and a positional argument
def g():
    yield
g.__code__ = gi
g(1, x=1)

# Test that a generator function can be called with a keyword argument
# and a positional argument
def g():
    yield
g.__code__ = gi
g(1, x=1)

# Test that a generator function can be called with a keyword argument
# and a positional argument
def g():
    yield
