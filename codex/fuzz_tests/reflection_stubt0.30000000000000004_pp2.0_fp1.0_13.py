fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = '__main__'
fn.__dict__ = {}
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__closure__ = None
fn.__annotations__ = {}
fn.__globals__ = {}
fn.__doc__ = None
fn.__text_signature__ = None
fn.__get__ = None
fn.__set__ = None
fn.__delete__ = None
fn.__set_name__ = None
fn.__init__ = None
fn.__new__ = None
fn.__init_subclass__ = None
fn.__prepare__ = None
fn.__class__ = function
fn.__subclasses__ = []
fn.__delattr__ = None
fn.__dir__ = None
fn.__eq__ = None
fn.__format__ = None
fn.__ge__ = None
fn.__getattribute__ = None
fn.__gt__
