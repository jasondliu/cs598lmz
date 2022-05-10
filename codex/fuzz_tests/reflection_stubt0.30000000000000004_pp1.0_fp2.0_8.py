fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = None

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = 42

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = "not a code object"

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = b"not a code object"

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = bytearray(b"not a code object")

# Issue #18078: segfault when __code__ is not a code object
def f():
    pass
f.__code__ = memoryview(b"not a
