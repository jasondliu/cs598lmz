fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'fn'
fn.__module__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = None
