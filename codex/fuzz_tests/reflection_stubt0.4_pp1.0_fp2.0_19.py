fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__qualname__ = gi.gi_qualname
fn.__annotations__ = gi.gi_annotations
fn.__kwdefaults__ = gi.gi_kwdefaults
fn.__defaults__ = gi.gi_defaults
fn.__closure__ = gi.gi_closure
fn.__globals__ = gi.gi_globals
fn.__dict__ = gi.gi_frame.f_locals
fn.__doc__ = gi.gi_code.co_consts[0] if gi.gi_code.co_consts else None
fn.__module__ = gi.gi_code.co_filename
return fn
</code>

