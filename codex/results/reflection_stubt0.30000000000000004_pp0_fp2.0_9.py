fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #22139: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = None
f()

# Issue #22139: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = 42
f()

# Issue #22139: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = "not a code object"
f()

# Issue #22139: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = (1, 2, 3)
f()

# Issue #22139: segfault when calling a function with a bad __code__
# attribute.
def f():
    pass
f.__code__ = bytearray(b"not a code object")
f()

# Issue #22139:
