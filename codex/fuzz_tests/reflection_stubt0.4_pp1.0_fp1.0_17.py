fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should raise a TypeError.
try:
    fn()
except TypeError:
    print('TypeError')
