fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that generators don't have a __code__ attribute.
gi = (i for i in ())
try:
    gi.__code__
except AttributeError:
    pass
else:
    raise AssertionError("Generator should not have a __code__ attribute")

# Test that generators don't have a __code__ attribute.
gi = (i for i in ())
try:
    gi.__code__
except AttributeError:
    pass
else:
    raise AssertionError("Generator should not have a __code__ attribute")

# Test that generators don't have a __code__ attribute.
gi = (i for i in ())
try:
    gi.__code__
except AttributeError:
    pass
else:
    raise AssertionError("Generator should not have a __code__ attribute")

# Test that generators don't have a __code__ attribute.
gi = (i for i in ())
try:
    gi.__code__
except AttributeError:
    pass
else:
    raise Assert
