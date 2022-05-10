import types
# Test types.FunctionType
def test_types_functiontype():
    def f(x):
        return x
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(f, types.LambdaType)
    assert not isinstance(f, types.UnboundMethodType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(f, types.ModuleType)
    assert not isinstance(f, types.GeneratorType)
    assert not isinstance(f, types.TracebackType)
    assert not isinstance(f, types.FrameType)
    assert not isinstance(f, types.CodeType)
    assert not isinstance(f, types.MappingProxyType)
    assert not isinstance(f, types.SimpleNamespace)
    assert not isinstance(f, types.DynamicClassAttribute)
    assert not isinstance(f, types.MemberDescriptorType)
    assert not isinstance(f
