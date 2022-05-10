fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24076: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = None
f()

# Issue #24076: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = 1
f()

# Issue #24076: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = "abc"
f()

# Issue #24076: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = b"abc"
f()

# Issue #24076: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = bytearray(b"abc")
f()

# Issue #24076: segf
