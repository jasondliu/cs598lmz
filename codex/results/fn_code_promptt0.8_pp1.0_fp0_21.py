fn = lambda: None
# Test fn.__code__
fn.__code__  # Make sure it's a code object
fn.__code__.co_argcount  # Expected number of arguments
fn.__code__.co_varnames  # variable names
# Test fn.__globals__
# We need to define `foo` in `fn.__globals__`
fn.__globals__['foo'] = "bar"
fn.foo  # Should return "bar"
# Test fn.__closure__
# We need to define a closure
fn.__closure__  # Should be None
fn.__closure__[0].cell_contents  # Should be "bar"

# Test fn.__name__
fn.__name__  # This is a string, we should be able to set it
fn.__name__ = "fn"
fn.__name__  # Should now be fn
# Test fn.__defaults__
fn.__defaults__  # Should be None
fn.__defaults__ = (42,)
fn()  # Should be 42
fn(1)  # Should be 1
# Test
