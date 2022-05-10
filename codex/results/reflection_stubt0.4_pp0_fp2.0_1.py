fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', '', 0, b'')
fn.__code__.co_varnames = gi.gi_code.co_varnames = ()
fn.__code__.co_argcount = gi.gi_code.co_argcount = 0
fn()

# Issue #29180: ensure that the 'code' attribute of a coroutine
# is writable.
def f():
    yield
f.__code__ = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', '', 0, b'')

# Issue #29180: ensure that the 'gi_code' attribute of a generator
# is writable.
g = (i for i in ())
g.gi_code = types.CodeType(0, 0, 0, 0, b'', b'', (), (), (), '', '', 0, b'')

# Issue #29180: ensure that the '__code__' attribute of a
