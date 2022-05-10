fn = lambda: None
# Test fn.__code__ to make sure we can check for __defaults__:
if hasattr(FunctionType, '__code__'):
    try:
        assert_true(hasattr(fn.__code__, '__defaults__'))
    except AssertionError:
        assert_true(hasattr(fn.func_code, 'co_defaults'))
else:
    assert_true(hasattr(fn.func_code, 'co_defaults'))


def test_scan_kwelta
