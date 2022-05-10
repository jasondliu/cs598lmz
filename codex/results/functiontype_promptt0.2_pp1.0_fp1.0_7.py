import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x, y: x, types.FunctionType)
assert not isinstance(lambda x, y, z: x, types.FunctionType)
assert not isinstance(lambda *args: None, types.FunctionType)
assert not isinstance(lambda **kwargs: None, types.FunctionType)
assert not isinstance(lambda *args, **kwargs: None, types.FunctionType)
assert not isinstance(lambda x, *args: None, types.FunctionType)
assert not isinstance(lambda x, **kwargs: None, types.FunctionType)
assert not isinstance(lambda x, *args, **kwargs: None, types.FunctionType)
assert not isinstance(lambda x, y, *args: None, types.FunctionType)
assert not isinstance(lambda x, y, **kwargs: None, types.FunctionType)
assert not isinstance(
