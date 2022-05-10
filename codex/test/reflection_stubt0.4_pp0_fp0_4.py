fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# __code__ is not writable
try:
    fn.__code__ = fn.__code__
except TypeError:
    pass
