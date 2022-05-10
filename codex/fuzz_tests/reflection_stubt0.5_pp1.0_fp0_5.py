fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__qualname__ = gi.gi_qualname
fn.__module__ = gi.gi_frame.f_globals['__name__']
fn.__doc__ = gi.gi_code.co_consts[0] if gi.gi_code.co_consts else None
fn.__defaults__ = gi.gi_code.co_consts[1] if gi.gi_code.co_consts else None
fn.__kwdefaults__ = gi.gi_code.co_consts[2] if gi.gi_code.co_consts else None
fn.__annotations__ = gi.gi_code.co_consts[3] if gi.gi_code.co_consts else None
return fn
</code>

