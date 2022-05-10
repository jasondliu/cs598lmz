fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = None
f()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 42
f()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = "not a code object"
f()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = b"not a code object"
f()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = (1, 2, 3)
f()

# Issue #23048: Segfault when __code__ is not a code object
def f():
    pass
f.__code__ = b"\x01\x02\
