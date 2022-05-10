fn = lambda: None
# Test fn.__code__.co_flags
test_fn.__code__.co_flags = 0
test_fn.__code__.co_flags = 0xFFFF
test_fn.__code__.co_flags = 0xFFFFFFFF

# Test fn.__code__.co_nlocals
test_fn.__code__.co_nlocals = 0
test_fn.__code__.co_nlocals = 0xFFFF
test_fn.__code__.co_nlocals = 0xFFFFFFFF

# Test fn.__code__.co_stacksize
test_fn.__code__.co_stacksize = 0
test_fn.__code__.co_stacksize = 0xFFFF
test_fn.__code__.co_stacksize = 0xFFFFFFFF

# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno = 0
test_fn.__code__.co_firstlineno = 0xFFFF
test_fn.__code__.co_firstlineno = 0xFFFFFFFF
