fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
assert gi.gi_frame is None
