fn = lambda: None
# Test fn.__code__.co_argcount
setattr(fn, '__code__', lambda: None)
setattr(fn.__code__, 'co_argcount', 3)
assert fn.__code__.co_argcount == 3

# Test fn.__code__.co_nlocals
setattr(fn.__code__, 'co_nlocals', 4)
assert fn.__code__.co_nlocals == 4

# Test fn.__code__.co_varnames
setattr(fn.__code__, 'co_varnames', ('a', 'b', 'c', 'd'))
assert fn.__code__.co_varnames == ('a', 'b', 'c', 'd')

# Test fn.__code__.co_varnames[i]
assert fn.__code__.co_varnames[1] == 'b'

# Test fn.__code__.co_varnames[i] = 5
fn.__code__.co_varnames[1] = 'e'
assert fn.__code
