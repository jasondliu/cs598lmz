fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_code = fn
gi.gi_frame = gi
gi.gi_running = True
eval('fn.__code__.gi_frame.gi_code.__globals__["_"] = 1', {'fn': fn, '_': 2})

# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
