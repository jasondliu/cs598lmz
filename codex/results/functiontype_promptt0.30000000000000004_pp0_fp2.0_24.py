import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert isinstance(object, types.FunctionType)
assert isinstance(object(), types.FunctionType)
assert isinstance(types.FunctionType, types.FunctionType)
assert isinstance(types.FunctionType(lambda: None, {}, None, None, None), types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(int, types.LambdaType)
assert not isinstance(object, types.LambdaType)
assert not isinstance(object(), types.LambdaType)
assert not isinstance(types.LambdaType, types.LambdaType)
assert not isinstance(types.LambdaType(lambda: None, {}, None, None, None), types.LambdaType)

# Test types.Generator
