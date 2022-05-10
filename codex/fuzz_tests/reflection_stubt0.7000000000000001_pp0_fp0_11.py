fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
get_overflow_flag()
