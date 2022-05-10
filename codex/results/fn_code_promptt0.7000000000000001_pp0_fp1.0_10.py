fn = lambda: None
# Test fn.__code__
fn.__code__ = code
fn.__code__ = None
# Test fn.__defaults__
fn.__defaults__ = ()
fn.__defaults__ = None
# Test fn.__annotations__
fn.__annotations__ = {'a': 1}
fn.__annotations__ = None
# Test fn.__kwdefaults__
fn.__kwdefaults__ = {'a': 1}
fn.__kwdefaults__ = None
# Test fn.__globals__
fn.__globals__ = {'a': 1}
fn.__globals__ = None
# Test fn.__closure__
fn.__closure__ = (1,)
fn.__closure__ = None
# Test fn.__dict__
fn.__dict__ = {'a': 1}
fn.__dict__ = None
# Test fn.__name__
fn.__name__ = 'foo'
fn.__name__ = None
# Test fn.__qualname__
fn.__qualname__ = 'foo'
fn.__qualname__ = None
