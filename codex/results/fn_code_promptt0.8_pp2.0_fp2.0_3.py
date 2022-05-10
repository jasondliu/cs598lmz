fn = lambda: None
# Test fn.__code__.co_argcount
mock_fn.__code__.co_argcount = 2
# Test fn.__code__.co_varnames
mock_fn.__code__.co_varnames = ("foo",)


def test_show_function_signature():
    """
    Assert that show_function_signature() works as intended.
    """

    assert show_function_signature(mock_fn) == "<function mock_fn(foo, *args, **kwargs)>"
    assert show_function_signature(mock_fn, call_args=(1,)) == "<function mock_fn(foo=1, *args, **kwargs)>"
    assert show_function_signature(mock_fn, call_args=(1, 2)) == "<function mock_fn(1, 2, *args, **kwargs)>"
    assert show_function_signature(mock_fn, call_args=(1, 2), call_kwargs={"key": "value"}) == "<function mock_fn(1, 2, *args, key='
