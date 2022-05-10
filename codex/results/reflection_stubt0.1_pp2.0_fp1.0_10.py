fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = None

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = 1

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = "abc"

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = b"abc"

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = bytearray(b"abc")

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = memoryview(b"abc")

# Issue #26897: __code__ should be read-only
def f(): pass
f.__code__ = range(10)

# Issue #26897: __code__ should be read-only

