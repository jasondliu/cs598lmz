import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x, y: x, types.FunctionType)
assert isinstance(lambda x, y, z: x, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x, y: x, types.LambdaType)
assert isinstance(lambda x, y, z: x, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert isinstance(g.__code__, types.
