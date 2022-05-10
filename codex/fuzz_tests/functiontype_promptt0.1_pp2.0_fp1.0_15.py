import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
