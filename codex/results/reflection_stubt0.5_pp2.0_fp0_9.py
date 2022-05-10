fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'module'
fn.__dict__ = {'__name__': 'fn', '__module__': 'module'}
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None

# fn.__text_signature__ = '()'

# fn.__code__.co_varnames = ()
# fn.__code__.co_argcount = 0

# fn.__code__.co_cellvars = ()
# fn.__code__.co_freevars = ()

# fn.__code__.co_nlocals = 0
# fn.__code__.co_stacksize = 0

# fn.__code__.co_flags = 0x0040
# fn.__code__.co_code = b''
# fn.__code__.co
