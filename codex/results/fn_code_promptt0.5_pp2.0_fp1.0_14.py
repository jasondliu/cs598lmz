fn = lambda: None
# Test fn.__code__.co_varnames
setattr(fn, '__code__', lambda: None)
setattr(fn.__code__, 'co_varnames', ('x', 'y', 'z'))
assert get_args(fn) == ['x', 'y', 'z']

# Test fn.__code__.co_argcount
setattr(fn.__code__, 'co_argcount', 2)
assert get_args(fn) == ['x', 'y']

# Test fn.__code__.co_varnames and fn.__code__.co_argcount
setattr(fn.__code__, 'co_varnames', ('x',))
assert get_args(fn) == ['x']


# Test get_arg_values
def fn(a, b, c):
    return a, b, c

# Test fn.__code__.co_varnames
setattr(fn, '__code__', lambda: None)
setattr(fn.__code__, 'co_varnames', ('a', 'b', 'c'
