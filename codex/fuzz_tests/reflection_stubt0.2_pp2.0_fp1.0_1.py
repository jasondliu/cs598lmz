fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following should raise a TypeError, but instead raises a SystemError
# because the code object is not a proper code object.

def fn():
    pass
fn.__code__ = (i for i in ())
fn()
