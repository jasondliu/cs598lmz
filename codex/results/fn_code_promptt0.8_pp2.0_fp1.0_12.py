fn = lambda: None
# Test fn.__code__.co_nlocals
_test_fn.__code__.co_nlocals = 0
raise NotImplementedError
"""
    with pytest.raises(NotImplementedError):
        ic(source)

def test_function_code_co_nlocals_unsupported():
    if PY3:
        pytest.skip("Unsupport on Py3")
    source = """
_test_fn = lambda: None
# Test fn.__code__.co_nlocals
_test_fn.__code__.co_nlocals = 1
raise NotImplementedError
"""
    with pytest.raises(NotImplementedError):
        ic(source)

def test_function_code_co_nlocals_supported():
    if PY3:
        pytest.skip("Unsupport on Py3")
    source = """
_test_fn = lambda: None
# Test fn.__code__.co_nlocals
_test_fn.__code__.co_nlocals = 0
print(_test_fn.
