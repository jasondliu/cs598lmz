fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
# Test fn.__code__.co_argcount
# Test fn.__code__.co_consts
# Test fn.__code__.co_names
# Test fn.__code__.co_nlocals
# Test fn.__code__.co_stacksize
# Test fn.__code__.co_flags
# Test fn.__code__.co_firstlineno
# Test fn.__code__.co_lnotab
# Test fn.__code__.co_freevars
# Test fn.__code__.co_cellvars

# Test fn.__code__.co_varnames
test_fn.__code__.co_varnames = (1, 2)
try:
    test_fn.__code__.co_varnames
except TypeError:
    print('TypeError')

# Test fn.__code__.co_argcount
test_fn.__code__.co_argcount = (1, 2)
try:

