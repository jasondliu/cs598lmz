fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = tuple(range(0x1000))
# Test fn.__code__.co_names
test_fn.__code__.co_names = tuple(range(0x1000))
# Test fn.__code__.co_consts
test_fn.__code__.co_consts = tuple(range(0x1000))
# Test fn.__code__.co_cellvars
test_fn.__code__.co_cellvars = tuple(range(0x1000))
# Test fn.__code__.co_freevars
test_fn.__code__.co_freevars = tuple(range(0x1000))
# Test fn.__code__.co_stacksize
test_fn.__code__.co_stacksize = 0x1000
# Test fn.__code__.co_flags
test_fn.__code__.co_flags = 0x1000


# Test fn.__closure__
def closure_test_fn():
    closure_test_fn
