fn = lambda: None
# Test fn.__code__ against the expected values
test_fn.__code__ is test_fn.__code__
test_fn.__code__ is test_fn.__code__
hasattr(test_fn.__code__, "co_freevars")
hasattr(test_fn.__code__, "co_cellvars")
# Test fn.__code__ against the expected values
test_fn.__code__.co_nlocals
test_fn.__code__.co_stacksize
test_fn.__code__.co_flags
test_fn.__code__.co_code
test_fn.__code__.co_consts
test_fn.__code__.co_names
test_fn.__code__.co_varnames
test_fn.__code__.co_filename
test_fn.__code__.co_name
test_fn.__code__.co_firstlineno
test_fn.__code__.co_lnotab
test_fn.__code__.co_freevars
test_fn.__code__.co_cell
