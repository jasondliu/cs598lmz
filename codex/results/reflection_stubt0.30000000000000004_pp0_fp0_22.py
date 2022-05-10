fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__closure__ = None
fn.__globals__ = {}
fn.__dict__ = {}
fn.__module__ = '__main__'
fn.__doc__ = None
fn.__text_signature__ = None

# Function with a closure
def fn():
    x = 1
    def g():
        return x
    return g

fn = fn()
fn.__code__ = fn.__closure__[0].cell_contents.__code__
fn.__name__ = 'g'
fn.__qualname__ = 'fn.<locals>.g'
fn.__annotations__ = {}
fn.__kwdefaults__ = None
fn.__defaults__ = ()
fn.__closure__ = fn.__closure__
fn.__globals__ = globals()
fn.__dict__ =
