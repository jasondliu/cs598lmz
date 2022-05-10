fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = None
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = 42
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = "foo"
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = b"foo"
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = bytearray(b"foo")
fn()

# Issue #17077: crash when __code__ is not a code object
def fn(): pass
fn.__code__ = memoryview(b"foo")
fn()

# Issue #17077: crash when __code__ is not a
