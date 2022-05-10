fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn()

# Frame objects
import types
co = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
f = types.FrameType(None, None, None, None)
f.f_code = co

# Traceback objects
tb = None
while tb is not None:
    tb = tb.tb_next

# Slice objects
try:
    slice
except NameError:
    pass
else:
    slice(1, 2, 3)

# Cell objects
def f():
    x = 3
    def g():
        print(x)
    return g
fn = f()
cell = fn.__closure__[0]

# Weakref objects
import weakref
r = weakref.ref(fn)

# Generator objects
def f():
    yield 1
gen = f()
gen.gi_code = co

# Custom objects
class C:
    def __init__(self,
