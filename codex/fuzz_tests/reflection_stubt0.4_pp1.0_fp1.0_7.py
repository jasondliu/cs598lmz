fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that we don't crash when creating a function with a generator
# that has a non-tuple code object.
gi.__code__ = None
fn.__code__ = gi
fn()

# Test that we don't crash when creating a function with a generator
# that has a non-tuple code object, and that has a non-tuple code
# object.
fn.__code__ = gi
gi.__code__ = fn
fn()

# Test that we don't crash when creating a function with a generator
# that has a non-tuple code object, and that has a non-tuple code
# object, and that has a non-tuple code object.
gi.__code__ = fn
fn.__code__ = gi
gi.__code__ = fn
fn()

# Test that we don't crash when creating a function with a generator
# that has a non-tuple code object, and that has a non-tuple code
# object, and that has a non-tuple code object, and that has a
# non-t
