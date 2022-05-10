fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that __code__ can be set to a function
fn = lambda: None
fn.__code__ = fn
fn()

# Test that __code__ can be set to a method
fn = lambda: None
fn.__code__ = fn.__code__.__get__(fn)
fn()

# Test that __code__ can be set to a method
fn = lambda: None
fn.__code__ = fn.__code__.__get__(fn, fn)
fn()

# Test that __code__ can be set to a method
fn = lambda: None
fn.__code__ = fn.__code__.__get__(fn, fn.__class__)
fn()

# Test that __code__ can be set to a method
fn = lambda: None
fn.__code__ = fn.__code__.__get__(fn, fn.__class__())
fn()

# Test that __code__ can be set to a method
fn = lambda: None
fn.__code__ = fn.__code__.__get__(
