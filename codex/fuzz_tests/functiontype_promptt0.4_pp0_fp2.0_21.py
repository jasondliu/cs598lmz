import types
# Test types.FunctionType

def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.ModuleType)
    assert not isinstance(f, types.TracebackType)
    assert not isinstance(f, types.FrameType)
    assert not isinstance(f, types.CodeType)
    assert not isinstance(f, types.TypeType)
    assert not isinstance(f, types.SliceType)
    assert not isinstance(f, types.XRangeType)
    assert not isinstance(f, types.EllipsisType)
    assert not isinstance(f, types.DictProxyType)
    assert not isinstance(f, types.NotImplementedType)
    assert not isinstance(f, types.GetSetDescriptorType)
    assert not isinstance(f, types.
