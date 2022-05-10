fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_frame)()
fn.__globals__ = {}
fn.__closure__ = (None,)
fn.__code__.co_argcount = 0
fn.__code__.co_flags = 67
fn.__code__.co_code = b'\x00\x00S\x00'
fn.__code__.co_consts = ()
fn.__code__.co_names = ()
fn.__code__.co_varnames = ()
fn.__code__.co_filename = "<stdin>"
fn.__code__.co_name = "None"
fn.__code__.co_firstlineno = 1
fn.__code__.co_lnotab = b'\x00\x01'
fn.__code__.co_freevars = ()
fn.__code__.co_cellvars = ()
fn.__code__ = types.CodeType(fn.__code__.co_argcount,
                             fn.__code__.co_kwonlyargcount
