fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = None
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = "not a code object"
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = 1
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = object()
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not used if it is not a code object.
fn.__code__ = (i for i in ())
fn()

# Test that the code object is not used if it is not a code object.
