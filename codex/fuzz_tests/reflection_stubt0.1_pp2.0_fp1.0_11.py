fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'fn'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = ()
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__module__ = '__main__'
fn.__qualname__ = 'fn'
fn.__get__ = lambda: None
fn.__set__ = lambda: None
fn.__delete__ = lambda: None
fn.__init__ = lambda: None
fn.__new__ = lambda: None
fn.__prepare__ = lambda: None
fn.__instancecheck__ = lambda: None
fn.__subclasscheck__ = lambda: None
fn.__init_subclass__ = lambda: None
fn.__class_getitem__ = lambda: None
fn.__subclasshook__ = lambda: None
fn.__delattr__ = lambda: None
fn.__dir__ = lambda: None
fn.__format__ = lambda:
