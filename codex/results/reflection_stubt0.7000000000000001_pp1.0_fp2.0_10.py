fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
gi.gi_code.co_code = b'X'

try:
    fn()
except TypeError:
    pass
