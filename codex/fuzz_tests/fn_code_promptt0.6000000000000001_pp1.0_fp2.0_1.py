fn = lambda: None
# Test fn.__code__.co_argcount
fn.__code__ = type('code', (object,), {'co_argcount': 0})
# Test fn.__code__.co_varnames
fn.__code__.co_varnames = ()

# Test fn.__closure__
fn.__closure__ = ()

# Test fn.__globals__
fn.__globals__ = {}

# Test fn.__module__
fn.__module__ = '__main__'

# Test fn.__defaults__
fn.__defaults__ = ()

# Test fn.__kwdefaults__
fn.__kwdefaults__ = None

# Test fn.__dict__
fn.__dict__ = {}

# Test fn.__annotations__
fn.__annotations__ = {}

# Test fn.__get__
fn.__get__(None)
fn.__get__(None, object)

# Test fn.__set__
fn.__set__(None)
fn.__set__(None, object)

# Test fn
