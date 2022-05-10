fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Test that __code__ is not a function.
try:
    fn.__code__()
except TypeError:
    print('TypeError')

# Test that __code__ is not a function.
try:
    fn.__code__.__code__()
except TypeError:
    print('TypeError')
