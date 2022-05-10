fn = lambda: None
# Test fn.__code__
fn.__code__
# Test fn.__defaults__
fn.__defaults__
# Test fn.__globals__
fn.__globals__
# Test fn.__kwdefaults__
fn.__kwdefaults__
# Test fn.__name__
fn.__name__
# Test fn.__qualname__
fn.__qualname__

# Test fn.__get__
fn.__get__(1)
# Test fn.__getattribute__
fn.__getattribute__('__name__')
# Test fn.__setattr__
fn.__setattr__('__name__', 'new_name')
# Test fn.__delattr__
fn.__delattr__('__name__')
# Test fn.__dir__
fn.__dir__()
# Test fn.__call__
fn.__call__()
# Test fn.__repr__
fn.__repr__()
# Test fn.__str__
fn.__str__()
# Test fn.__format__
fn.__format__('s')
#
