import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(test_function_type, types.FunctionType)
    assert isinstance(lambda: None, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(1, types.FunctionType)
    assert not isinstance(1.0, types.FunctionType)
    assert not isinstance('', types.FunctionType)
    assert not isinstance(u'', types.FunctionType)
    assert not isinstance(object(), types.FunctionType)
    assert not isinstance([], types.FunctionType)
    assert not isinstance((), types.FunctionType)
    assert not isinstance({}, types.FunctionType)
    assert not isinstance(set(), types.FunctionType)
    assert not isinstance(frozenset(), types.FunctionType)
    assert not isinstance(bytearray(b''), types.FunctionType)
    assert not isinstance(memoryview(b''), types.FunctionType)
