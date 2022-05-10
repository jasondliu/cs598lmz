fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, '__code__', lambda: None)
# Test fn.__code__.co_varnames and fn.__code__.co_argcount
setattr(fn.__code__, 'co_varnames', None)
setattr(fn.__code__, 'co_argcount', None)

# Test fn.__code__.__call__
fn2 = fn.__code__

# Test fn.__defaults__
setattr(fn, '__defaults__', None)
# Test fn.__kwdefaults__
setattr(fn, '__kwdefaults__', None)

# Test fn.__dict__
setattr(fn, '__dict__', None)
# Test fn.__self__
setattr(fn, '__self__', None)
# Test fn.__qualname__
setattr(fn, '__qualname__', None)

# Test fn.__annotations__
setattr(fn, '__annotations__', None)

# Test fn -> True
x = fn is True
