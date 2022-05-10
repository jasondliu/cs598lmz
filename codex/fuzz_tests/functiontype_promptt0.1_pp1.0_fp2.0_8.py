import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f, types.CodeType)
assert not isinstance(f, types.TracebackType)
assert not isinstance(f, types.FrameType)
assert not isinstance(f, types.GetSetDescriptorType)
assert not isinstance(f, types.MemberDescriptorType)
assert not isinstance(f, types.WrapperDescriptorType)

# Test types.LambdaType
g = lambda: None
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(g, types.MethodType)
assert isinstance(g
