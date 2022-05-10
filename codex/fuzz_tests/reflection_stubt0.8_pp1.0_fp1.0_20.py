fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = type(None)()
fn.__closure__ = gi.gi_frame.f_code.co_freevars
fn.func_defaults = ()
fn.__dict__ = {}
fn.func_dict = {}
fn.__name__ = fn.__qualname__ = 'function_name'
fn.__annotations__ = {}
fn.__module__ = 'module_name'
fn.__globals__ = None
fn.__doc__ = 'docstring'
glob = {'fn': fn}
code = compile('docstring', 'module_name', 'exec')
exec(code, glob, glob)
