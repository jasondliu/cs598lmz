fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'

# Make sure the code object is not owned by the function.
fn.__code__ = fn.__code__

# Make sure the function is not owned by the code object.
