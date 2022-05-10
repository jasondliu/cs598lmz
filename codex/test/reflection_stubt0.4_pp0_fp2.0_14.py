fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# This used to raise a SystemError, but now it raises a TypeError.
try:
    fn()
except TypeError:
    print("TypeError")
