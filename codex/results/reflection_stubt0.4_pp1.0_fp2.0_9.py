fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = ''
fn.__globals__ = {'__builtins__': {}, '__name__': '__main__', '__doc__': None, '__package__': None}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__module__ = '__main__'
fn.__qualname__ = 'fn'
fn.__get__ = &lt;method-wrapper '__get__' of function object at 0x7f4b4f4e4268&gt;
fn.__set__ = &lt;method-wrapper '__set__' of function object at 0x7f4b4f4e4268&gt;
fn.__delete__ = &lt;method-wrapper '__delete__' of function object at 0x7f4b4f4e4268&gt;
fn.__slots__ = ()
fn
