fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', code)

# Test fn.__closure__
fn.__closure__ = (cell,)

# Test fn.__globals__
fn.__globals__ = {}

# Test fn.__defaults__
fn.__defaults__ = ()

# Test fn.__kwdefaults__
fn.__kwdefaults__ = {}

# Test fn.__annotations__
fn.__annotations__ = {}

# Test fn.__dict__
fn.__dict__ = {}

# Test fn.__name__
fn.__name__ = 'fn'

# Test fn.__qualname__
fn.__qualname__ = 'fn'

# Test fn.__module__
fn.__module__ = '__main__'

# Test fn.__doc__
fn.__doc__ = 'doc'

# Test fn.__text_signature__
fn.__text_signature__ = '()'

# Test fn.__get__
fn.__get__
