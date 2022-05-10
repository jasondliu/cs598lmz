fn = lambda: None
# Test fn.__code__
fn.__code__ == "foo"
# Test fn.__closure__
fn.__closure__
fn.__closure__ == "foo"
# Test fn.__name__
fn.__name__ == "foo"
# Test fn.__qualname__
fn.__qualname__ == "foo"
# Test fn.__self__
fn.__self__ == "foo"
fn.__self__
# Test fn.__module__
fn.__module__ == "foo"
fn.__module__
fn.__doc__ == "foo"
# Test fn.__globals__
fn.__globals__ == "foo"
# Test fn.__dict__
fn.__dict__ == "foo"
# Test fn.__weakref__
fn.__weakref__ == "foo"
