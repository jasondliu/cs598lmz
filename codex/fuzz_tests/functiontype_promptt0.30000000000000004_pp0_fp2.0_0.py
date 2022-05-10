import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(test_function_type, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(42, types.FunctionType)
    assert not isinstance(2.5, types.FunctionType)
    assert not isinstance('q', types.FunctionType)
    assert not isinstance(u'q', types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(test_function_type, types.BuiltinFunctionType)
    assert not isinstance(None, types.BuiltinFunctionType)
    assert not isinstance(42, types.BuiltinFunctionType)
    assert not isinstance(2.5, types.BuiltinFunctionType)
    assert not isinstance('q', types.BuiltinFunctionType)
    assert not isinstance(u'q', types.BuiltinFunctionType)
    assert not isinstance(f, types.UnboundMethodType)

