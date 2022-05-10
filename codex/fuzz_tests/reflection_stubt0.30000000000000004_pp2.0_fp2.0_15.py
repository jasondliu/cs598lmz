fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = 'module'

try:
    fn()
except TypeError:
    print('TypeError')
