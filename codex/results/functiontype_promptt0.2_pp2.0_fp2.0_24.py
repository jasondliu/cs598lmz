import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.UnboundMethodType)
assert not isinstance(f, types.CodeType)
assert not isinstance(f, types.TracebackType)
assert not isinstance(f, types.FrameType)
assert not isinstance(f, types.GetSetDescriptorType)
assert not isinstance(f, types.MemberDescriptorType)
assert not isinstance(f, types.WrapperDescriptorType)
assert not isinstance(f, types.MethodDescriptorType)
assert not isinstance(f, types.DictProxyType)
assert not isinstance(f, types.NotImplementedType)
assert not isinstance(f, types.EllipsisType)
assert not isinstance(f, types.ModuleType)
assert
