import types
# Test types.FunctionType
def func(): pass
assert isinstance(func, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(map, types.FunctionType)
assert not isinstance(42, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(map, types.FunctionType)
assert not isinstance(types.FunctionType, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(func, types.LambdaType)
assert not isinstance(42, types.LambdaType)
assert not isinstance(None, types.LambdaType)
assert not isinstance(map, types.LambdaType)
assert not isinstance(types.LambdaType, types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(3)), types.GeneratorType)
assert not isinstance(func, types.GeneratorType)
assert not isinstance(lambda: None
