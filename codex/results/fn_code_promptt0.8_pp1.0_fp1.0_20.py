fn = lambda: None
# Test fn.__code__ changes
setattr(fn, '__code__', 'code')
assert_equal(fn.__code__, 'code')

# Test fn.__defaults__ changes
setattr(fn, '__defaults__', 'defaults')
assert_equal(fn.__defaults__, 'defaults')

# Test fn.__dict__ changes
setattr(fn, '__dict__', 'dict')
assert_equal(fn.__dict__, 'dict')

# Test fn.__closure__ changes
setattr(fn, '__closure__', 'closure')
assert_equal(fn.__closure__, 'closure')

# Test fn.__globals__ changes
setattr(fn, '__globals__', 'globals')
assert_equal(fn.__globals__, 'globals')

# Test fn.__doc__ changes
setattr(fn, '__doc__', 'doc')
assert_equal(fn.__doc__, 'doc')

# Test fn.__name__ changes
setattr(fn, '__name__',
