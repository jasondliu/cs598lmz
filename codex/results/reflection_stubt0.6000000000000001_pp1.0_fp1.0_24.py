fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = c
fn.__globals__ = gi.gi_frame.f_globals
fn.__closure__ = gi.gi_frame.f_locals['__closure__']
fn.__name__ = c.co_name
fn.__doc__ = c.co_consts[0] if c.co_consts else None
fn.__defaults__ = c.co_consts[1] if c.co_consts else None
fn.__dict__ = {}
fn.__annotations__ = c.co_consts[2] if c.co_consts and len(c.co_consts) > 2 else None
return fn

def make_cell(value):
    fn = (lambda x: lambda: x)(value)
    return fn.__closure__[0]

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

class Cell(object):
    def __init__(self,
