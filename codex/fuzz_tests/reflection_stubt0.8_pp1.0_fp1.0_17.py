fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = co
assert fn.func_code is co
assert gi.gi_code is co
assert gi.__code__ is co

# try to mess with the cellvars, freevars and argcount
co.co_cellvars = (1, 2, 3)
assert fn.func_code.co_cellvars == (1, 2, 3)
co.co_freevars = (1, 2, 3)
assert fn.func_code.co_freevars == (1, 2, 3)
co.co_argcount = 42
assert fn.func_code.co_argcount == 42

# set a new cellvars value, it only changes co_cellvars if co_cellvars is None
# (done when the function is wrapped by new.function)
co.co_cellvars = None
co.co_freevars = None
fn.__closure__ = (None, None)
assert co.co_cellvars == ()
assert co.co_freevars == ()

# do it again, but
