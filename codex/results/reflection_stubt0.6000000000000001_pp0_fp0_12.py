fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# func_code is a read-only property
try:
    fn.__code__ = 1
except TypeError:
    print('TypeError')

# func_code is a read-only property
try:
    del fn.__code__
except TypeError:
    print('TypeError')
