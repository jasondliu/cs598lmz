fn = lambda: None
# Test fn.__code__
def test_fn_code():
    assert fn.__code__.co_name == '<lambda>'
    assert fn.__code__.co_argcount == 0

# Test functions.__di
