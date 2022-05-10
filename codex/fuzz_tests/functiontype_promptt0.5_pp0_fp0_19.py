import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(int, type)
assert isinstance(type, type)
assert not isinstance(1, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(int, types.LambdaType)
# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(lambda x: x, types.GeneratorType)
# Test types
