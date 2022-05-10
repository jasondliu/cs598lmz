fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = gi.gi_closure
fn.__name__ = gi.gi_name
fn.__dict__ = gi.gi_frame.f_locals
fn.__doc__ = gi.gi_frame.f_code.co_consts[0] if gi.gi_frame.f_code.co_consts else None
fn.__module__ = gi.gi_frame.f_globals.get('__name__', '__main__')
fn.__defaults__ = gi.gi_frame.f_code.co_varnames[:gi.gi_frame.f_code.co_argcount]
fn.__kwdefaults__ = {
    k: v.cell_contents
    for k, v in zip(gi.gi_frame.f_code.co_varnames[gi.gi_frame.f_code.co_argcount:], gi.gi_frame.f_locals.values())
    if isinstance(v, types.Cell)
}

