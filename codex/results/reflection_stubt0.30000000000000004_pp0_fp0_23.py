fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = ''
fn.__module__ = '__main__'
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__closure__ = None
fn.__annotations__ = {}
fn.__globals__ = globals()
fn.__dict__ = {}
fn.__qualname__ = 'fn'

# The following is a function that takes an argument.
def fn(a):
    pass

fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__dict__ = {}
fn.__doc__ = ''
fn.__module__ = '__main__'
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__closure__ = None
fn.__annotations__ = {}
fn.__globals__ = globals()
fn.__dict__ = {}
fn.__qualname__ = 'fn'

#
