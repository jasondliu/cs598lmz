fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Test that the __code__ attribute can be a generator
fn()

# Test that a generator can be the __code__ attribute of a function.
fn.__code__()

# Test that the __code__ attribute can be set to None
fn.__code__ = None

# Test that __code__ can be set to None and then reset to a generator
fn.__code__ = None
fn.__code__ = gi
fn()

# Test that __code__ can be set to a generator and then reset to None
fn.__code__ = gi
fn.__code__ = None

# Test that the __code__ attribute can be set and cleared multiple times
fn.__code__ = gi
fn.__code__ = None
fn.__code__ = gi
fn.__code__ = None

# Test that the __code__ attribute can be set to a value that is later deleted
fn.__code__ = gi
del gi
fn()

# Test that the __code__ attribute can be set to a value that is later overwritten
fn.__code
