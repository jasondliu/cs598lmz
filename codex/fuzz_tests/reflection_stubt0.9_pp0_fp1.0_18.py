fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Try to call the thing
try:
    fn()
except TypeError:
    print('TypeError')
