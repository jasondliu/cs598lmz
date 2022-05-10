fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__dict__ = {}
fn.__globals__ = {}
fn.__closure__ = None
fn.__doc__ = None
fn.__module__ = None
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__get__ = None
fn.__set__ = None
fn.__delete__ = None
fn.__prepare__ = None
fn.__init_subclass__ = None
fn.__class__ = type
fn.__dict__ = {}
fn.__weakref__ = None
fn.__slots__ = None
fn.__self__ = None
fn.__func__ = None

print(fn)
print(fn.__dict__)
print(fn.__closure__)
print(fn.__class__)
print(fn.__code__)
print(fn.__defaults__)
print(fn.__get__)
print(fn.__doc__)
print(fn.
