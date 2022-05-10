fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #12076: crash when __code__ is not a code object
def f(): pass
f.__code__ = None

# Issue #12077: crash when __code__ is not a code object
def f(): pass
f.__code__ = 1

# Issue #12078: crash when __code__ is not a code object
def f(): pass
f.__code__ = "abc"

# Issue #12079: crash when __code__ is not a code object
def f(): pass
f.__code__ = b"abc"

# Issue #12080: crash when __code__ is not a code object
def f(): pass
f.__code__ = bytearray(b"abc")

# Issue #12081: crash when __code__ is not a code object
def f(): pass
f.__code__ = memoryview(b"abc")

# Issue #12082: crash when __code__ is not a code object
def f(): pass
f.__code__ = object()

# Issue #12083
