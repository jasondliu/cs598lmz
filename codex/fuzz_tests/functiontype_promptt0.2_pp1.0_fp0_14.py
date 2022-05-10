import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x, y: x + y, types.FunctionType)
assert not isinstance(lambda x, y, z: x + y + z, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x, y: x + y, types.LambdaType)
assert isinstance(lambda x, y, z: x + y + z, types.LambdaType)
assert not isinstance(f, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
    yield 2
    yield 3
assert isinstance(g(), types.GeneratorType)
assert isinstance((x for x in range(10)), types.GeneratorType)
assert not
