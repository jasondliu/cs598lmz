import types
# Test types.FunctionType
assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(None, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(g, types.LambdaType)
assert not isinstance(3, types.LambdaType)
assert not isinstance("", types.LambdaType)
assert not isinstance(None, types.LambdaType)

# Test types.GeneratorType
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(g, types.GeneratorType)
assert not isinstance(lambda x: x, types.GeneratorType)
assert not isinstance(3, types.
