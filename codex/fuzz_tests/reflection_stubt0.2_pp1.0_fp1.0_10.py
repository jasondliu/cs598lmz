fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 42
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = 'foo'
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None
fn.__code__ = object()
fn()

# __code__ is not a code object
fn = lambda: None

