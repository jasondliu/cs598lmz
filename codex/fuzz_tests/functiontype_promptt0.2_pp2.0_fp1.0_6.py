import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.MethodType)

# Test types.GeneratorType
def h():
    yield
assert isinstance(h(), types.GeneratorType)
assert not isinstance(h(), types.FunctionType)
assert not isinstance(h(), types.BuiltinFunctionType)
assert not isinstance(h(), types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.LambdaType)
assert not isinstance(len, types.MethodType)


