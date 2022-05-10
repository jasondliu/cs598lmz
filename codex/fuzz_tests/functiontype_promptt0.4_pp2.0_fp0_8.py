import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(ord, types.BuiltinFunctionType)
    assert not isinstance(ord, types.FunctionType)
    assert not isinstance(ord, types.BuiltinMethodType)
    assert not isinstance(ord, types.MethodType)
    assert not isinstance(ord, types.LambdaType)

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert isinstance(str.upper, types.BuiltinMethodType)
    assert not isinstance(str.upper, types.FunctionType)
    assert not isinstance(str.upper, types.Built
