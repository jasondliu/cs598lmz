fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = None
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = "not a code object"
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = 1
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = 1.0
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = True
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn
