fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following should raise a TypeError
# fn.__code__ = lambda: None
# fn()

# The following should raise a TypeError
# fn.__code__ = 1
# fn()

# The following should raise a TypeError
# fn.__code__ = "string"
# fn()

# The following should raise a TypeError
# fn.__code__ = b"bytes"
# fn()

# The following should raise a TypeError
# fn.__code__ = 1.0
# fn()

# The following should raise a TypeError
# fn.__code__ = 1j
# fn()

# The following should raise a TypeError
# fn.__code__ = object()
# fn()

# The following should raise a TypeError
# fn.__code__ = [1, 2, 3]
# fn()

# The following should raise a TypeError
# fn.__code__ = (1, 2, 3)
# fn()

# The following should raise a TypeError
# fn.__code__ = {1
