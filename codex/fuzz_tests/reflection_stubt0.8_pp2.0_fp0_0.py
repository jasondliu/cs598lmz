fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__globals__ = gi.gi_frame.f_globals
fn.__name__ = gi.gi_code.co_name = '<lambda>'
fn.__defaults__ = gi.gi_code.co_consts[0] if args else None
fn.__kwdefaults__ = gi.gi_code.co_consts[1] if kwargs else None
return fn
