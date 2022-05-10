fn = lambda: None
# Test fn.__code__.co_filename
test_fn.__code__.co_filename = "foo.py"
# Test fn.__code__.co_name
test_fn.__code__.co_name = "foo"
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno = 1

# Test fn.__code__.co_flags
assert test_fn.__code__.co_flags == 0
# Test fn.__code__.co_nlocals
assert test_fn.__code__.co_nlocals == 0
# Test fn.__code__.co_stacksize
assert test_fn.__code__.co_stacksize == 1
# Test fn.__code__.co_varnames
assert tuple(test_fn.__code__.co_varnames) == ()
# Test fn.__code__.co_argcount
assert test_fn.__code__.co_argcount == 0
# Test fn.__code__.co_cellvars
assert tuple(test_fn.
