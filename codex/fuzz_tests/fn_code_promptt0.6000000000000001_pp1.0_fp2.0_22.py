fn = lambda: None
# Test fn.__code__
fn.__code__
fn.__code__.co_argcount
fn.__code__.co_varnames
# Test fn.__closure__
fn.__closure__
fn.__closure__[0].cell_contents
# Test fn.__defaults__
fn.__defaults__
# Test fn.__dict__
fn.__dict__
fn.__dict__['x'] = 3
fn.__dict__.get('x')
# Test fn.__globals__
fn.__globals__
fn.__globals__['__name__']
fn.__globals__['__file__']
fn.__globals__['__cached__']
# Test fn.__kwdefaults__
fn.__kwdefaults__
# Test fn.__name__
fn.__name__
# Test fn.__qualname__
fn.__qualname__
# Test fn.__self__
fn.__self__
# Test fn.__closure__
fn.__closure__
# Test fn.__code__
fn.__code
