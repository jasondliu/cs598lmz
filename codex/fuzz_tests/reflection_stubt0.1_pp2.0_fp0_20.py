fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = None
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = 1
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = "abc"
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = b"abc"
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = bytearray(b"abc")
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = memoryview(b"abc")
fn()

# Issue #23984: __code__ must be a code object
def fn(): pass
fn.__code__ = range(1)
