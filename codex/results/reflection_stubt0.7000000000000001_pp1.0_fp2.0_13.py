fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'test'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = None
fn.__dict__ = {'__dict__': 'something'}
fn.__closure__ = gi.gi_closure
fn.__doc__ = gi.gi_frame.f_code.co_consts[0] if gi.gi_frame and gi.gi_frame.f_code.co_consts else None
fn.__globals__ = gi.gi_frame.f_globals if gi.gi_frame else {}
fn.__name__ = gi.gi_code.co_name if gi.gi_code else None
fn.__qualname__ = gi.gi_code.co_name if gi.gi_code else None
fn.__module__ = fn.__globals__.get('__name__')
fn.__annotations
