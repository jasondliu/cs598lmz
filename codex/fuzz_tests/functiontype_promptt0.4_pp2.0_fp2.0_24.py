import types
# Test types.FunctionType
def test_types_FunctionType():
    assert isinstance(test_types_FunctionType, types.FunctionType)
    assert isinstance(test_types_FunctionType, types.BuiltinFunctionType)
    assert isinstance(test_types_FunctionType, types.BuiltinMethodType)
    assert isinstance(test_types_FunctionType, types.MethodType)
    assert isinstance(test_types_FunctionType, types.LambdaType)
    assert isinstance(test_types_FunctionType, types.CodeType)
    assert isinstance(test_types_FunctionType, types.TracebackType)
    assert isinstance(test_types_FunctionType, types.FrameType)
    assert isinstance(test_types_FunctionType, types.GetSetDescriptorType)
    assert isinstance(test_types_FunctionType, types.MemberDescriptorType)
    assert isinstance(test_types_FunctionType, types.WrapperDescriptorType)
    assert isinstance(test_types_FunctionType, types.MethodWrapperType)
    assert isinstance(test_types
