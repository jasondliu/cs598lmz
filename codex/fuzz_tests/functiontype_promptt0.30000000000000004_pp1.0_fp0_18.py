import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(42, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(object, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(42, types.BuiltinFunctionType)
    assert not isinstance(None, types.BuiltinFunctionType)
    assert not isinstance(object, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert not isinstance(len, types.BuiltinMethodType)

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert isinstance(len, types.BuiltinMethodType)
   
