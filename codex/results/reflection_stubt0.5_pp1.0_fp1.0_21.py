fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'foo'
fn.__dict__ = {}
fn.__doc__ = None
fn.__module__ = None
fn.__defaults__ = None
fn.__kwdefaults__ = None
fn.__closure__ = None
fn.__annotations__ = {}
fn.__globals__ = {}
fn.__qualname__ = 'foo'

# Test function without __code__ attribute
def foo():
    pass
del foo.__code__

# Test function with __code__ attribute that is not a code object
def bar():
    pass
bar.__code__ = 'foo'

# Test function with __code__ attribute that is a code object
def baz():
    pass
baz.__code__ = type(baz.__code__)

# Test function with __code__ attribute that is a code object with
# a custom type
class MyCode(type(baz.__code__)):
    pass

def qux():
    pass
qux.__code__ = MyCode(*qux
