fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16078: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = None
try:
    f()
except TypeError:
    pass

# Issue #16078: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = "not a code object"
try:
    f()
except TypeError:
    pass

# Issue #16078: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = b"not a code object"
try:
    f()
except TypeError:
    pass

# Issue #16078: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = bytearray(b"not a code object")
try:
    f()
except TypeError:
    pass
