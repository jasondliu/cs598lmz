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
assert not isinstance(f, types.FrameType)
assert not isinstance(f, types.TracebackType)
assert not isinstance(f, types.ModuleType)
assert not isinstance(f, types.GetSetDescriptorType)
assert not isinstance(f, types.MemberDescriptorType)
assert not isinstance(f, types.WrapperDescriptorType)
assert not isinstance(f, types.ClassType)
assert not isinstance(f, types.InstanceType)
assert not isinstance(f, types.TypeType)
assert not isinstance(f, types.XRangeType)
assert not isinstance(f, types.Sl
