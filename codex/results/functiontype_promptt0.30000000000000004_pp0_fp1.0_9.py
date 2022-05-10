import types
# Test types.FunctionType
def test_function_type():
    def foo():
        pass
    assert isinstance(foo, types.FunctionType)
    assert not isinstance(foo, types.BuiltinFunctionType)
    assert not isinstance(foo, types.MethodType)
    assert not isinstance(foo, types.BuiltinMethodType)
    assert not isinstance(foo, types.ModuleType)
    assert not isinstance(foo, types.TypeType)
    assert not isinstance(foo, types.TracebackType)
    assert not isinstance(foo, types.FrameType)
    assert not isinstance(foo, types.CodeType)
    assert not isinstance(foo, types.GeneratorType)
    assert not isinstance(foo, types.GetSetDescriptorType)
    assert not isinstance(foo, types.MemberDescriptorType)
    assert not isinstance(foo, types.DictProxyType)
    assert not isinstance(foo, types.WrapperDescriptorType)
    assert not isinstance(foo, types.NotImplementedType)
    assert not isinstance(
