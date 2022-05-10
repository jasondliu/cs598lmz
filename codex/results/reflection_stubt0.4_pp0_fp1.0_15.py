fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we can't do this with a function that has been called
# (it's too late to change the code then).
fn = lambda: None
fn()
try:
    fn.__code__ = gi
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to set __code__ on called function")

# Test that we can't do this with a function that has been called
# (it's too late to change the code then).
fn = lambda: None
fn()
try:
    del fn.__code__
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to del __code__ on called function")

# Test that we can't do this with a function that has been called
# (it's too late to change the code then).
fn = lambda: None
fn()
try:
    fn.__code__ = None
except TypeError:
    pass
else:
    raise RuntimeError("shouldn't be able to set __code__ to None on called function")


