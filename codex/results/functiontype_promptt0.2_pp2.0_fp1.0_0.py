import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(f(), types.FunctionType)
assert not isinstance(None, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f(), types.LambdaType)
assert not isinstance(None, types.LambdaType)

# Test types.GeneratorType
def g():
    yield
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f(), types.GeneratorType)
assert not isinstance(None, types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
assert not isinstance(f, types.CodeType)
assert not isinstance
