fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__['__builtins__'] = dict()
fn.__globals__['__builtins__']['object'] = object
code = fn.__code__
