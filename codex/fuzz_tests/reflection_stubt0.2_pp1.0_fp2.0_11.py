fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = '__main__'
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__dict__ = {}
fn.__closure__ = None
fn.__doc__ = None
fn.__globals__ = {}
fn.__get__ = None
fn.__set__ = None
fn.__delete__ = None
fn.__slots__ = ()
fn.__weakref__ = None
fn.__text_signature__ = None
fn.__init_subclass__ = None
fn.__class__ = function
fn.__subclasshook__ = None
fn.__init__ = None
fn.__new__ = None
fn.__prepare__ = None
fn.__instancecheck__ = None
fn.__subclasscheck__ = None
fn.__call__ = None
fn.__len__ = None
fn.__length_hint__ = None

