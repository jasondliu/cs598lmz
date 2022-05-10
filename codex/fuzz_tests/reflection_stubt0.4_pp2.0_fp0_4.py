fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator-iterator can be used as a code object.
# The code object should be usable as the __code__ attribute of a function.
# The generator-iterator should be usable as the __code__ attribute of a function.
# The function should be callable.

# Test that a generator-iterator can be used as a code object.
gi = (i for i in ())

# The code object should be usable as the __code__ attribute of a function.
fn = lambda: None
fn.__code__ = gi

# The generator-iterator should be usable as the __code__ attribute of a function.
fn = lambda: None
fn.__code__ = gi

# The function should be callable.
fn()
