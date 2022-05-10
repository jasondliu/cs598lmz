fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__qualname__ = 'foo'
fn.__module__ = 'bar'
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__annotations__ = {}
fn.__dict__ = {}
fn.__closure__ = None
fn.__doc__ = None
fn.__globals__ = {}
fn.__get__ = None
fn.__set__ = None
fn.__delete__ = None
fn.__slots__ = None
fn.__weakref__ = None
fn.__text_signature__ = None
fn.__self__ = None
fn.__func__ = None

# test __init__
assert fn.__init__ is None
# test __repr__
assert repr(fn) == '<function foo at 0x{:x}>'.format(id(fn))
# test __hash__
assert hash(fn) == hash(gi.gi_code)
# test __call__
assert fn() is None
# test __get
