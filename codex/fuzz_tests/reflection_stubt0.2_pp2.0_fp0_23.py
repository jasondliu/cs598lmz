fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = None

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = 1

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = "foo"

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = b"foo"

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = bytearray(b"foo")

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = memoryview(b"foo")

# Issue #16078: crash when __code__ is not a code object
def f(): pass
f.__code__ = object()

# Issue #16
