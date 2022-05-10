fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a stack overflow.
# fn.__code__ = fn.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__.__code__.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__.__code__

# This is a stack overflow.
# fn.__code__ = fn.__code__.__code__.__code__.__code__.__code__.__code__.__code__

# This is a stack overflow.
# fn
