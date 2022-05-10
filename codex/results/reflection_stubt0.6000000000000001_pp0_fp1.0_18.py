fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Verify that we can't set the code object to a value that's not compatible.
try:
    fn.__code__ = 1
except TypeError:
    pass
else:
    raise Exception("code object can be set to any value")
