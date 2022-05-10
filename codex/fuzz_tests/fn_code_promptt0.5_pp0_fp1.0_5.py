fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__ = mock.Mock()
fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__defaults__
fn.__defaults__ = (1, 2)
fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__closure__
fn.__closure__ = (mock.Mock(),) * 3
fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__globals__
fn.__globals__ = {'foo': 'bar'}
fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__doc__
fn.__doc__ = "This is a docstring"
fn.__code__.co_varnames = ('a', 'b', 'c')


# Test fn.__name__
fn.__name__ = "foo"
fn.__code__.co
