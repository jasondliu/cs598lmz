fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# It should be invalid to assign an invalid generator to a function's __code__ attribute.
fn = lambda: None
gi = (i for i in ())
del gi.gi_code
try:
    fn.__code__ = gi
    raise AssertionError("shouldn't be able to assign an invalid generator to a function's __code__ attribute")
except TypeError:
    pass

# It should be invalid to assign a non-generator to a function's __code__ attribute.
fn = lambda: None
try:
    fn.__code__ = None
    raise AssertionError("shouldn't be able to assign a non-generator to a function's __code__ attribute")
except TypeError:
    pass
