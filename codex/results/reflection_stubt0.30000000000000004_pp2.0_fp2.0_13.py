fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = None
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 1
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = []
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = {}
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = "a"
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = b"a"
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = bytearray(b"a")
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = memoryview(b"a")
fn()

# __code__ is
