fn = lambda: None
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn()
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn(1, 2, 3)
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn.__code__.co_argcount
# Test fn.__code__.co_argcount
# End of test

# Begin of test
def test_fn(*args, **kwargs):
    pass
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn()
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn(1, 2, 3)
# Test fn.__code__.co_argcount
# End of test

# Begin of test
test_fn.__code__.co_argcount
# Test fn.__code__.co_argcount
# End of test
