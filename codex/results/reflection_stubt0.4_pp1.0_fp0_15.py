fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__globals__ = globals()
fn.__name__ = '<lambda>'
fn.__dict__ = {}
fn.__closure__ = ()
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__module__ = '<string>'
fn.__doc__ = None
fn.__text_signature__ = None
fn.__qualname__ = '<lambda>'

# For the following functions, we need to modify the code object
# to include a __qualname__ attribute.

def f():
    pass
f.__code__.co_qualname = 'f'

def g():
    def h():
        pass
    h.__code__.co_qualname = 'g.h'

class A:
    def f():
        pass
    f.__code__.co_qualname = 'A.f'

    def g():
        def h():
            pass
        h.__code__.co_qualname =
