fn = lambda: None
# Test fn.__code__.co_zombieframe is False.
test_fn.__code__.co_zombieframe = None
# Test fn.__code__.co_zombieframe is True, _PyCode_GETCODE(fn.__code__) is NULL.
test_fn.__code__.co_zombieframe = True


# Test fn.__code__.co_zombieframe is True, _PyCode_GETCODE(fn.__code__) is
# not NULL.
def test_fn():
    pass

test_fn.__code__.co_zombieframe = True
