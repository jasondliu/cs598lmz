import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(types.FunctionType, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(1, types.LambdaType)
assert not isinstance(None, types.LambdaType)
assert not isinstance(object, types.LambdaType)
assert not isinstance(type, types.LambdaType)
assert not isinstance(types.LambdaType, types.LambdaType)

# Test types.GeneratorType
def f():
    yield 1
assert isinstance(f(), types.GeneratorType)
assert not isinstance(1, types.GeneratorType)
assert not is
