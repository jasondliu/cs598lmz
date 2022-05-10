import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType
assert type(f) is types.LambdaType
assert type(f) is types.UnboundMethodType
assert type(f) is types.ModuleType
assert type(f) is types.TracebackType
assert type(f) is types.FrameType
assert type(f) is types.CodeType
assert type(f) is types.DictProxyType
assert type(f) is types.NotImplementedType
assert type(f) is types.GetSetDescriptorType
assert type(f) is types.MemberDescriptorType
assert type(f) is types.WrapperDescriptorType
assert type(f) is types.MethodWrapperType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.DynamicClassAttribute
assert type(f) is types.ClassMethodDescriptorType
assert type(
