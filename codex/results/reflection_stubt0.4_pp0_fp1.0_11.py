fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should raise a TypeError, not a RecursionError
try:
    fn.__code__ = fn.__code__
except TypeError:
    print('TypeError')
except RecursionError:
    print('RecursionError')

# This should raise a TypeError, not a RecursionError
try:
    fn.__code__ = fn.__code__.__code__
except TypeError:
    print('TypeError')
except RecursionError:
    print('RecursionError')
