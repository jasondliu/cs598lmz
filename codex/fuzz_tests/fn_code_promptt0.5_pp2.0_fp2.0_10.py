fn = lambda: None
# Test fn.__code__
fn.__code__ = code
# Test fn.__closure__
fn.__closure__ = closure
# Test fn.__defaults__
fn.__defaults__ = defaults
# Test fn.__dict__
fn.__dict__ = dict
# Test fn.__doc__
fn.__doc__ = doc
# Test fn.__globals__
fn.__globals__ = globals
# Test fn.__name__
fn.__name__ = name
# Test fn.__self__
fn.__self__ = self
# Test fn.__module__
fn.__module__ = module
# Test fn.__qualname__
fn.__qualname__ = qualname

# Test fn.__code__.co_argcount
fn.__code__.co_argcount = argcount
# Test fn.__code__.co_cellvars
fn.__code__.co_cellvars = cellvars
# Test fn.__code__.co_code
fn.__code__.co_code = code
# Test fn.__code__.co_
