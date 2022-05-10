import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(1, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(int, types.LambdaType)
assert not isinstance(1, types.LambdaType)

# Test types.GeneratorType
assert not isinstance(f, types.GeneratorType)
assert not isinstance(lambda: None, types.GeneratorType)
assert not isinstance(int, types.GeneratorType)
assert not is
