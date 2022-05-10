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
fn.__code__ = 1
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = "string"
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = b"bytes"
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object.
fn = lambda: None
fn.__code__ = bytearray(b"bytearray")
fn()

# Test that the __code__ attribute of a function can be set to a
# non-code object
