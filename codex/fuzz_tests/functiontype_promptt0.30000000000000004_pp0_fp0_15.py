import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert isinstance(lambda x, y: x, types.FunctionType)
assert isinstance(lambda x, y=1: x, types.FunctionType)
assert isinstance(lambda x, y=1, *z: x, types.FunctionType)
assert isinstance(lambda x, y=1, *z, **t: x, types.FunctionType)
assert isinstance(lambda x, y=1, *, z=1: x, types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)
assert isinstance(lambda x, y: x, types.LambdaType)
assert isinstance(lambda x, y=1: x, types.LambdaType)

