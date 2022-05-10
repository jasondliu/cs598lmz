import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert type(f) == types.BuiltinFunctionType
assert type(f) == types.BuiltinMethodType
assert type(f) == types.MethodType
assert type(f) == types.LambdaType
assert type(f) == types.UnboundMethodType
assert type(f) == types.CodeType
assert type(f) == types.TracebackType
assert type(f) == types.FrameType
assert type(f) == types.BufferType
assert type(f) == types.DictProxyType
assert type(f) == types.NotImplementedType
assert type(f) == types.GetSetDescriptorType
assert type(f) == types.MemberDescriptorType
assert type(f) == types.WrapperDescriptorType
assert type(f) == types.CellType
assert type(f) == types.ClassType
assert type(f) == types.InstanceType
assert type(f) == types.MethodWrapperType
assert type(f) == types.Builtin
