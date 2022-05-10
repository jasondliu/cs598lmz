fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator function can be called with a keyword argument
def f(a):
    yield a

f(a=1)

# Test that a generator function can be called with a keyword argument
# and a default argument
def f(a, b=2):
    yield a

f(a=1)

# Test that a generator function can be called with a keyword argument
# and a default argument
def f(a, b=2):
    yield a

f(a=1, b=3)

# Test that a generator function can be called with a keyword argument
# and a default argument
def f(a, b=2):
    yield a

f(a=1, b=3)

# Test that a generator function can be called with a keyword argument
# and a default argument
def f(a, b=2):
    yield a

f(a=1, b=3)

# Test that a generator function can be called with a keyword argument
# and a default argument
def f(a, b=2):
   
