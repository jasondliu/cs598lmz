fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__doc__ = gi.gi_doc
fn.__module__ = gi.gi_frame.f_globals.get('__name__', '__main__')
fn.__dict__.update(gi.gi_frame.f_locals)
fn.func_closure = lambda: gi.gi_frame.f_locals['__closure__']
fn.func_code = lambda: gi.gi_code
fn.func_defaults = lambda: gi.gi_frame.f_locals['__defaults__']
fn.func_globals = lambda: gi.gi_frame.f_globals
fn.func_name = lambda: gi.gi_name
fn.func_doc = lambda: gi.gi_doc
fn.func_dict = lambda: fn.__dict__
fn.__closure__ = gi.gi_frame.f_locals['__closure__']
fn.__defaults__ = gi.gi_frame.
