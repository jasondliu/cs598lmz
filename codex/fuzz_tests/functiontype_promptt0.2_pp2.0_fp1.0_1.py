import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodDescriptorType)
assert not isinstance(f, types.MethodDescriptorType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
assert isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(g, types.MethodType)
assert not isinstance(g, types.BuiltinMethodDescriptorType)
assert not isinstance(g, types.MethodDescriptorType)

# Test types.GeneratorType
def h(): yield
assert isinstance(h(), types.GeneratorType)
assert not isinstance(h, types.GeneratorType)

# Test
