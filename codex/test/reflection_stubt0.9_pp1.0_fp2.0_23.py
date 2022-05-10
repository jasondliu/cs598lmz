fn = lambda: None
gi = (i for i in ())
fn.__code__ = tab = gi.gi_frame.f_code

