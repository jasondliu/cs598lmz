import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.CodeType)
assert isinstance(f, types.TracebackType)
assert isinstance(f, types.FrameType)
assert isinstance(f, types.BufferType)
assert isinstance(f, types.DictProxyType)
assert isinstance(f, types.NotImplementedType)
assert isinstance(f, types.GetSetDescriptorType)
assert isinstance(f, types.MemberDescriptorType)
assert isinstance(f, types.WrapperDescriptorType)
assert isinstance(f, types.MethodWrapperType)
assert isinstance(f, types.MethodDescriptorType)
assert isinstance(f, types.ModuleType)
assert isinstance(f, types.FileType)
assert
