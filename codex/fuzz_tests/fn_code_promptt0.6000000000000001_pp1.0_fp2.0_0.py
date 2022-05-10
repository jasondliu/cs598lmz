fn = lambda: None
# Test fn.__code__
setattr(fn, '__code__', code_obj)
assert fn.__code__ is code_obj

# Test fn.__code__.co_filename
assert fn.__code__.co_filename == '<code>'
setattr(fn.__code__, 'co_filename', 'abc')
assert fn.__code__.co_filename == 'abc'

# Test fn.__code__.co_name
assert fn.__code__.co_name == '<lambda>'
setattr(fn.__code__, 'co_name', 'def')
assert fn.__code__.co_name == 'def'

# Test fn.__code__.co_firstlineno
assert fn.__code__.co_firstlineno == 1
setattr(fn.__code__, 'co_firstlineno', 2)
assert fn.__code__.co_firstlineno == 2

# Test fn.__code__.co_varnames
assert fn.__code__.co_varnames == ()
setattr(fn.__code__
