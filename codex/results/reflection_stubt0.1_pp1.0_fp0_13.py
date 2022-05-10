fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified when it is not a generator
# object.
def fn():
    pass
fn.__code__ = fn.__code__
fn()

# Test that the code object is not modified when it is not a generator
# object.
def fn():
    pass
fn.__code__ = fn
fn()

# Test that the code object is not modified when it is not a generator
# object.
def fn():
    pass
fn.__code__ = fn.__code__.__code__
fn()

# Test that the code object is not modified when it is not a generator
# object.
def fn():
    pass
fn.__code__ = fn.__code__.__code__.__code__
fn()

# Test that the code object is not modified when it is not a generator
# object.
def fn():
    pass
fn.__code__ = fn.__code__.__code__.__code__.__code__
fn()

# Test that the code object is not modified when it is not
