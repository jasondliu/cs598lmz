fn = lambda: None
# Test fn.__code__
test_fn.__code__
# Check types
assert isinstance(test_fn.__code__, types.CodeType)
# Test fn.__code__.co_name
test_fn.__code__.co_filename
# Check types
assert isinstance(test_fn.__code__.co_filename, str)
# Test fn.__code__.co_name
test_fn.__code__.co_firstlineno
# Check types
assert isinstance(test_fn.__code__.co_firstlineno, int)
# Test fn.__code__.co_name
test_fn.__code__.co_argcount
# Check types
assert isinstance(test_fn.__code__.co_argcount, int)
# Test fn.__code__.co_name
test_fn.__code__.co_nlocals
# Check types
assert isinstance(test_fn.__code__.co_nlocals, int)
# Test fn.__code__.co_name
test_fn.__code__.co_varnames

