import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
assert not isinstance(func, types.BuiltinFunctionType)
assert not isinstance(func, types.BuiltinMethodType)
assert not isinstance(func, types.MethodType)
assert not isinstance(func, types.LambdaType)
assert not isinstance(func, types.GeneratorType)
assert not isinstance(func, types.CodeType)
assert not isinstance(func, types.TracebackType)
assert not isinstance(func, types.FrameType)
assert not isinstance(func, types.GetSetDescriptorType)
assert not isinstance(func, types.MemberDescriptorType)
assert not isinstance(func, types.WrapperDescriptorType)
# Test types.BuiltinFunctionType
assert not isinstance(abs, types.FunctionType)
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.BuiltinMethodType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(
