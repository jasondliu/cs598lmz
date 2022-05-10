fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__module__ = 'mod'
fn.__dict__ = dict(a=1)
fn.__defaults__ = (2, 3)
