fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__annotations__ = {}
fn.__doc__ = None
fn.__globals__ = {}
fn.__closure__ = None
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__get__ = lambda self, obj, type=None: self
fn.__set__ = lambda self, obj, value: None
fn.__delete__ = lambda self, obj: None
fn.__init__ = lambda self, *args, **kwargs: None
fn.__new__ = lambda cls, *args, **kwargs: object.__new__(cls)
fn.__reduce__ = lambda self: (fn, ())
fn.__reduce_ex__ = lambda self, protocol: (fn, ())
fn.__getattribute__ = lambda self, name: object.__getattribute__(self, name)
fn.__setattr
