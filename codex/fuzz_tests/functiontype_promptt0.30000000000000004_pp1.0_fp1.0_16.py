import types
# Test types.FunctionType
def test_function_type():
    assert types.FunctionType(lambda x: x, globals(), 'foo')
    assert types.FunctionType(lambda x: x, globals(), 'foo', None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None, None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None, None, None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None, None, None, None, None)
    assert types.FunctionType(lambda x: x, globals(), 'foo', None, None, None, None, None, None, None, None)
    assert types
