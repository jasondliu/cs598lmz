fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert fn.__code__ is gi

# Test that the code object is not modified
def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert fn.__code__ is gi

# Test that the code object is not modified
def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert fn.__code__ is gi

# Test that the code object is not modified
def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified
assert fn.__code__ is gi

# Test that the code object is not modified
def fn():
    pass

gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the
