fn = lambda: None
# Test fn.__code__ is mutable
test_fn.__code__ = test_fn.__code__

# Test fn.__code__.co_consts is mutable
test_fn.__code__.co_consts = (1, 2, 3)

# Test fn.__code__.co_cellvars, co_freevars, co_names and co_varnames
# are mutable
test_fn.__code__ = test_fn.__code__
