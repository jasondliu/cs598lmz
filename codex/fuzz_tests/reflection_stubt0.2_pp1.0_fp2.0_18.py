fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 1
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = "abc"
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 1.0
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = True
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = None
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = type
fn()

# __code__ is not a code object
fn = lambda: None
fn.__
