fn = lambda: None
# Test fn.__code__ is writable
def test_writable_code():
    try:
        fn.__code__ = 42
    except TypeError:
        pass
    else:
        assert False, '__code__ should not be writable'
# Test fn.__code__ is not None
def test_code_is_not_none():
    assert fn.__code__ is not None, '__code__ should not be None'
# Test fn.__code__.co_code is not None
def test_code_code_is_not_none():
    assert fn.__code__.co_code is not None, '__code__.co_code should not be None'
# Test fn.__code__.co_code is bytes
def test_code_code_is_bytes():
    assert isinstance(fn.__code__.co_code, bytes), '__code__.co_code should be bytes'
# Test fn.__code__.co_code is not empty
def test_code_code_is_not_empty():
    assert len(fn.__code__.co_code)
