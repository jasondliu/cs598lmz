fn = lambda: None
# Test fn.__code__.co_filename
setattr(fn, '__code__', fn.__code__)

# Test fn.__code__.co_filename
setattr(fn.__code__, 'co_filename', 'foo')

# Test fn.__code__.co_firstlineno
setattr(fn.__code__, 'co_firstlineno', 1)

# Test fn.__code__.co_name
setattr(fn.__code__, 'co_name', 'foo')

# Test fn.__code__.co_varnames
setattr(fn.__code__, 'co_varnames', ('a', 'b', 'c'))

# Test fn.__code__.co_argcount
setattr(fn.__code__, 'co_argcount', 3)

# Test fn.__code__.co_flags
setattr(fn.__code__, 'co_flags', 0)

# Test fn.__code__.co_code
setattr(fn.__code__, 'co_code', b'foo')


