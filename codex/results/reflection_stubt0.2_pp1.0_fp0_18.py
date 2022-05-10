fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Code objects are not callable
try:
    fn()
except TypeError:
    print("TypeError")
