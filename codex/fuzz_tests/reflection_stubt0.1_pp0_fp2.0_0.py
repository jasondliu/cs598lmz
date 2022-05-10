fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is closed.
gi = (i for i in ())
gi.close()
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is exhausted.
gi = (i for i in ())
list(gi)
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is exhausted
# and closed.
gi = (i for i in ())
gi.close()
list(gi)
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is closed
# and exhausted.
gi = (i for i in ())
list(gi)
gi.close()
fn.__code__ = gi
fn()

# Test that the code object is not modified when the generator is closed
# and exhausted.
gi = (i for i in ())
gi.close()
list(gi)
gi.close()
fn.__code__ = gi
fn()

#
