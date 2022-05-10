import types
# Test types.FunctionType
assert isinstance(func, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance([], types.FunctionType)
assert not isinstance(None, types.FunctionType)

# Test types.LambdaType
assert not isinstance(func, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(3, types.LambdaType)
assert not isinstance([], types.LambdaType)
assert not isinstance(None, types.LambdaType)

# Test types.GeneratorType
assert not isinstance(func, types.GeneratorType)
assert not isinstance(lambda x: x, types.GeneratorType)
assert not isinstance(3, types.GeneratorType)
assert not isinstance([], types.GeneratorType)
assert not isinstance(None, types.GeneratorType)

# Test types.BuiltinFunctionType
assert not isinstance(func, types.BuiltinFunction
