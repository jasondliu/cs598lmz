fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
try:
    fn()
except TypeError:
    print('TypeError')
