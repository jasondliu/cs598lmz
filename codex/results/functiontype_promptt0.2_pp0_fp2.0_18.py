import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.GeneratorType
def g():
    yield 1
assert not isinstance(g, types.FunctionType)
assert isinstance(g, types.GeneratorType)
assert not isinstance(g, types.LambdaType)
assert not isinstance(g, types.MethodType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)

# Test types.LambdaType
assert not isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda: None, types.GeneratorType)
assert isinstance(lambda: None
