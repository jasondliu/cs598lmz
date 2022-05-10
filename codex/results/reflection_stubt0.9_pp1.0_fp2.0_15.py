fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
inspect.getmodule(fn)
raise Exception("unreachable code")
