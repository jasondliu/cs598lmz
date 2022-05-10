fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
del gi
