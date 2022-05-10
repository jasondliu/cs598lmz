fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_stacksize = 3
fn.__code__.co_consts[1] = lambda: None
# Test fn.__code__.co_consts
fn.__code__.co_names[0] = 'foo'
# Test fn.__code__.co_names
fn.__code__.co_varnames = 'foo'
# Test fn.__code__.co_varnames
fn.__closure__ = [None]
fn.__annotations__ = {'foo': None}
# Test fn.__annotations__
fn.__kwdefaults__ = {'foo': None}
# Test fn.__kwdefaults__
fn.__defaults__ = (None,)
# Test fn.__defaults__
fn.__dict__['__name__'] = 'bar'
# Test fn.__name__
fn.__dict__['__doc__'] = 'bar'
# Test fn.__doc__
fn.__dict__['__dict__'] = 'bar'
# Test fn.__
