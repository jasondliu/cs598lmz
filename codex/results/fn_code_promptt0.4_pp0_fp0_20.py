fn = lambda: None
# Test fn.__code__.co_filename
test_fn.__code__.co_filename = 'test_fn'
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno = 0

# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = ('a', 'b', 'c')

# Test fn.__code__.co_argcount
test_fn.__code__.co_argcount = 3

# Test fn.__code__.co_flags
test_fn.__code__.co_flags = 0

# Test fn.__code__.co_lnotab
test_fn.__code__.co_lnotab = b'\x00\x01\x01\x01\x01\x01'

# Test fn.__code__.co_freevars
test_fn.__code__.co_freevars = ('d',)

# Test fn.__code__.co_cellvars
test_fn.__code__
