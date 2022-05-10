fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = (None,)
fn.__globals__ = {'__builtins__': None, '__name__': '__main__', '__doc__': None, '__package__': None}
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__qualname__ = '<lambda>'
fn()

# __code__
# __closure__
# __globals__
# __dict__
# __defaults__
# __kwdefaults__
# __annotations__
# __qualname__

import dis
dis.dis(fn)
