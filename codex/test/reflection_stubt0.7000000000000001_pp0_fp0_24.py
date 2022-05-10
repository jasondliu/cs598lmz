fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = gi.gi_frame.f_code
