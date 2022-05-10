fn = lambda: None
# Test fn.__code__.co_firstlineno
test_fn.__code__.co_firstlineno

# Test fn.__code__.co_varnames as tuple
tuple(test_fn.__code__.co_varnames)

# Test fn.__code__.co_consts as tuple
tuple(test_fn.__code__.co_consts)

# Test fn.__code__.co_names as tuple
tuple(test_fn.__code__.co_names)


# Test fn.__code__.co_flags
test_fn.__code__.co_flags

# Test fn.__code__.co_argcount
test_fn.__code__.co_argcount


# PY-12459
# test how to get the attribute co_lnotab from the funcation __code__
# attribute co_lnotab is added to function function in Python 3.6
def test_co_lnotab():
    pass

if hasattr(test_co_lnotab.__code__, "co_lnotab"
