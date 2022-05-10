fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = type('code', (object,), {'co_argcount': 2})
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ('x', 'y')

# Test fn.__globals__
fn.__globals__ = type('namespace', (object,), {'bar': 2})

# Test fn.__defaults__
fn.__defaults__ = (1,)

# Test fn.__closure__
fn.__closure__ = (lambda: None,)
fn.__closure__[0].cell_contents = 'foo'

# Test fn.__dict__
fn.__dict__ = {'foo': 2}

# Test fn.__module__
fn.__module__ = '__main__'

# Test fn.__name__
fn.__name__ = 'foo'

# Test fn.__doc__
fn.__doc__ = 'foo doc string'

# Test fn.__annotations__
fn.__annotations
