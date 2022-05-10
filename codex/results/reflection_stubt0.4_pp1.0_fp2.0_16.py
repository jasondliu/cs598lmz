fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not copied
assert fn.__code__ is gi

# Test that a new generator is not created
assert fn.__code__ is fn.__code__

# Test that the code object is not copied when the lambda is
# called with arguments
fn = lambda x: x
gi = (i for i in ())
fn.__code__ = gi
fn(1)

# Test that the code object is not copied
assert fn.__code__ is gi

# Test that a new generator is not created
assert fn.__code__ is fn.__code__

# Test that the code object is not copied when the lambda is
# called with arguments
fn = lambda x, y: x
gi = (i for i in ())
fn.__code__ = gi
fn(1, 2)

# Test that the code object is not copied
assert fn.__code__ is gi

# Test that a new generator is not created
assert fn.__code__ is fn.__code__
