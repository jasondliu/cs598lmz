fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code  # TODO: remove
setattr(fn, 'gi_code', gi.gi_code)  # TODO: remove
fn.__name__ = '<lambda>'
del gi  # TODO: remove
