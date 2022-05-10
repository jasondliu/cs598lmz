fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__doc__ = gi.gi_doc
fn.__module__ = gi.gi_module
fn.__dict__ = gi.gi_frame.f_locals
fn.__closure__ = gi.gi_frame.f_locals['__closure__']
fn.__annotations__ = gi.gi_frame.f_locals['__annotations__']
return fn
</code>

