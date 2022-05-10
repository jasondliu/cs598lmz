fn = lambda: None
# Test fn.__code__.co_filename
test_fn.__code__.co_filename = 'dummy'
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno = 0
# Test fn.__code__.co_flags
test_fn.__code__.co_flags = 0
# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = ('dummy', 'dummy')

print('[TRACE] test_fn.__code__.co_filename    : %s' % test_fn.__code__.co_filename)
print('[TRACE] test_fn.__code__.co_firstlineno : %s' % test_fn.__code__.co_firstlineno)
print('[TRACE] test_fn.__code__.co_flags       : %s' % test_fn.__code__.co_flags)
print('[TRACE] test_fn.__code__.co_varnames    : %s' % test_fn
