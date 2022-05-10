import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f, types.CodeType)
assert not isinstance(f, types.TracebackType)
assert not isinstance(f, types.FrameType)
assert not isinstance(f, types.GetSetDescriptorType)
assert not isinstance(f, types.MemberDescriptorType)
assert not isinstance(f, types.WrapperDescriptorType)

# Test types.BuiltinFunctionType
assert not isinstance(print, types.FunctionType)
assert isinstance(print, types.BuiltinFunctionType)
assert not isinstance(print, types.BuiltinMethodType)
assert not isinstance(print, types.MethodType)
assert not isinstance(print,
