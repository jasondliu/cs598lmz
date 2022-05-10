fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be set to None
fn = lambda: None
fn.__code__ = None
fn()

# Test that __code__ can be set to a function
fn = lambda: None
fn.__code__ = fn
fn()

# Test that __code__ can be set to a function with a non-function __code__
fn = lambda: None
fn.__code__ = fn
fn.__code__ = fn
fn()

# Test that __code__ can be set to a function with a function __code__
fn = lambda: None
fn.__code__ = fn
fn.__code__ = fn
fn()

# Test that __code__ can be set to a function with a non-function __code__
fn = lambda: None
fn.__code__ = fn
fn.__code__ = fn
fn()

# Test that __code__ can be set to a function with a function __code__
fn = lambda: None
fn.__code__ = fn
fn.__code__ = fn
fn()

# Test that
