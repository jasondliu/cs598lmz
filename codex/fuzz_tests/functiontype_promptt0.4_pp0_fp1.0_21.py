import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.LambdaType)
    assert not isinstance(f, types.UnboundMethodType)
    assert not isinstance(f, types.CodeType)
    assert not isinstance(f, types.TracebackType)
    assert not isinstance(f, types.FrameType)
    assert not isinstance(f, types.GetSetDescriptorType)
    assert not isinstance(f, types.MemberDescriptorType)
    assert not isinstance(f, types.WrapperDescriptorType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(len, types.FunctionType)
    assert
