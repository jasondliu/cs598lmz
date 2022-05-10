fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__qualname__ = '<lambda>'
fn.__module__ = '__main__'
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__closure__ = None
fn.__dict__ = {}
fn.__globals__ = {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '<stdin>', '__cached__': None}
fn.__code__ = <code object <lambda> at 0x7f4f4a4a4c20, file "<stdin>", line 1>
fn.__code__.co_argcount = 0
fn.__code__.co_kwonly
