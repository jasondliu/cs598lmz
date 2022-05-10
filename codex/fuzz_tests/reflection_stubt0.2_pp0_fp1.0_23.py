fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()

# Test that __code__ can be set to a function
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__()

# Test that __code__ can be set to a function with a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn.__code__()

# Test that __code__ can be set to a function with a __code__
# that has a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn.__code__.__code__.__code__ = lambda: None
fn.__code__()

# Test that __code__ can be set to a function with a __code__
# that has a __code__ that has a __code__
fn = lambda: None
fn.__code__ = lambda: None
fn.__code__.__code__ = lambda: None
fn.__code__.__
