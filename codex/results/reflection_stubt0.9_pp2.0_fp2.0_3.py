fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
ob = fn()
