fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'docstring'
fn.__dict__ = {}
fn.__module__ = 'module'
fn.__defaults__ = ()
