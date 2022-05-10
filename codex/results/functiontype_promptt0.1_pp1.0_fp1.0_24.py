import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x, y: x, types.FunctionType)
assert not isinstance(lambda x, y, z: x, types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x, y: x, types.LambdaType)
assert isinstance(lambda x, y, z: x, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)
assert not isinstance(f(), types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
