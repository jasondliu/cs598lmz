import types
# Test types.FunctionType
def f(a, b):
    return a + b

assert type(f) is types.FunctionType
assert not isinstance(f, types.FunctionType)
assert not issubclass(types.FunctionType, type)
# Test types.BuiltinFunctionType
assert type(int) is types.BuiltinFunctionType
assert not isinstance(int, types.BuiltinFunctionType)
assert not issubclass(types.BuiltinFunctionType, type)
# Test types.LambdaType
f = lambda a, b: a + b

assert type(f) is types.LambdaType
assert not isinstance(f, types.LambdaType)
assert not issubclass(types.LambdaType, type)
# Test types.GeneratorType
def g(a, b):
    yield a
    yield b

assert type(g(1, 2)) is types.GeneratorType
assert not isinstance(g(1, 2), types.GeneratorType)
assert not issubclass(types.GeneratorType, type)
# Test types.CoroutineType
as
