fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
assert fn.__code__ is gi.gi_code
assert fn.__name__ == 'fn'
assert fn.__doc__ == 'doc'
