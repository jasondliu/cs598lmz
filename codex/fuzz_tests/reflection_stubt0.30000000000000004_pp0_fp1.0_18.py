fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be set to None.
fn.__code__ = None
fn()

# Test that __code__ can be set to a function.
fn.__code__ = fn
fn()

# Test that __code__ can be set to a function with a __code__ attribute.
fn.__code__ = fn.__code__
fn()

# Test that __code__ can be set to a function with a __code__ attribute that
# is a function.
fn.__code__ = fn.__code__.__code__
fn()

# Test that __code__ can be set to a function with a __code__ attribute that
# is a function with a __code__ attribute.
fn.__code__ = fn.__code__.__code__.__code__
fn()

# Test that __code__ can be set to a function with a __code__ attribute that
# is a function with a __code__ attribute that is a function.
fn.__code__ = fn.__code__.__code__.__code__.__code__
