fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(
    0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
fn.__name__ = gi.gi_name = '_'
gi.gi_frame = fn.__globals__ = fn.__closure__ = ()
gi.gi_running = False
gi.__doc__ = ''
gi.__name__ = '<genexpr>'
gi.__qualname__ = '<genexpr>'
gi.__module__ = '__main__'
globals().update(locals())
del b, types, locals, globals, i, gi, fn
