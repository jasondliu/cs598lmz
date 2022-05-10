fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# __code__ is not writable
try:
    fn.__code__ = 0
except TypeError:
    print('TypeError')

# __code__ is not deletable
try:
    del fn.__code__
except TypeError:
    print('TypeError')
