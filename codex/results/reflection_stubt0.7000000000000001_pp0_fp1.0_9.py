fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# Verify that a generator is not considered as a function.
fn = lambda: None
gi = (i for i in ())
assert not hasattr(gi, '__code__')
try:
    gi.__code__()
except AttributeError:
    pass

# Verify that a generator is not considered as a function.
fn = lambda: None
gi = (i for i in ())
assert not hasattr(gi, '__code__')
try:
    gi.__code__()
except AttributeError:
    pass
