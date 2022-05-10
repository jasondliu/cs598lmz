fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #23984: test that the __code__ attribute of a function is read-only
def f(): pass
try:
    f.__code__ = None
except TypeError:
    pass
else:
    raise Exception("__code__ attribute should be read-only")

# Issue #23984: test that the __code__ attribute of a function is writable
# when the function is created with types.FunctionType()
def f(): pass
fn = types.FunctionType(f.__code__, f.__globals__, "fn", (), f.__closure__)
fn.__code__ = None

# Issue #23984: test that the __code__ attribute of a function is writable
# when the function is created with types.FunctionType() and has a closure
def f(): pass
fn = types.FunctionType(f.__code__, f.__globals__, "fn", (), (None,))
fn.__code__ = None

# Issue #23984: test that the __code__ attribute of a
