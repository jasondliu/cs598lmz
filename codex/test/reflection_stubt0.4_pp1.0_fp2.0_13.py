fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# The following code should raise a TypeError.

try:
    fn()
except TypeError:
    print("TypeError")

# This code should raise a SystemError.

