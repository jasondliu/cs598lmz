fn = lambda: None
# Test fn.__code__ is an attribute of fn.
fn.__code__
# Test fn.__code__ is writable.
fn.__code__ = lambda: None
# Test fn.__code__ is a method of fn.
fn.__code__()
# Test fn.__code__ is callable.
fn.__code__(1, 2, 3)
