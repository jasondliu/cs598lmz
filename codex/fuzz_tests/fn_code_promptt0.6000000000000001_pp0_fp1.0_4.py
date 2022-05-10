fn = lambda: None
# Test fn.__code__.co_varnames
test_fn.__code__ = type(test_fn.__code__)(
    0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', (), (), ()
)

# Check that we can create a new code object with a name that is not a string
# (ex: a function)
# Test code.co_name
test_code.co_name = lambda x: x
# Test code.co_filename
test_code.co_filename = lambda x: x
# Test code.co_lnotab
test_code.co_lnotab = lambda x: x
# Test code.co_freevars
test_code.co_freevars = lambda x: x
# Test code.co_cellvars
test_code.co_cellvars = lambda x: x
# Test code.co_varnames
test_code.co_varnames = lambda x: x

# Check that we can create a new frame object with a name that is not a string
# (ex: a function)
#
