fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__name__ = gi.gi_frame.f_code.co_name
fn.__dict__ = gi.gi_frame.f_globals
fn.__doc__ = gi.gi_frame.f_code.co_consts[0] if gi.gi_frame.f_code.co_consts else ''
fn.__module__ = gi.gi_frame.f_globals.get('__name__', '__main__')
