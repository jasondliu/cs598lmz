fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = None
fn.__globals__ = globals()
fn.__closure__ = None
fn.__doc__ = None
fn.__text_signature__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__module__ = '__main__'
fn.__qualname__ = 'fn'
fn.__self__ = None
fn.__get__ = lambda self, instance, owner: self
fn.__set__ = lambda self, instance, value: None
fn.__delete__ = lambda self, instance: None
fn.__init__ = lambda self, *args, **kwargs: None
fn.__new__ = lambda cls, *args, **kwargs: None
fn.__prepare__ = lambda cls, bases, **kwargs: None
fn.__instancecheck__ = lambda self, instance: False
fn.__subclasscheck__ = lambda self, subclass: False
fn.__call
