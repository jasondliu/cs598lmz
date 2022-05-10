fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__globals__ = gi.gi_frame.f_globals
fn.__name__ = gi.gi_code.co_name = '<lambda>'
fn.__defaults__ = gi.gi_code.co_consts[0] if args else None
fn.__kwdefaults__ = gi.gi_code.co_consts[1] if kwargs else None
fn.__closure__ = gi.gi_code.co_freevars = (c for c in ())
fn.__annotations__ = gi.gi_code.co_names = {}

def closure(fn):
    fn.__closure__ = (c.cell_contents for c in fn.__closure__)
    return fn

def call(fn, *args, **kwargs):
    return types.FunctionType(fn.__code__, fn.__globals__, fn.__name__, fn.__defaults__, fn.__closure__)(*args, **
