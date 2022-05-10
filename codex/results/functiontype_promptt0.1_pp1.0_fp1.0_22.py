import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance("", types.FunctionType)
assert not isinstance(b"", types.FunctionType)
assert not isinstance(bytearray(b""), types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(type(None), types.FunctionType)
assert not isinstance(type(object), types.FunctionType)
assert not isinstance(type(type), types.FunctionType)
assert not isinstance(type(type(None)), types.FunctionType)
assert not isinstance(type(type(object)), types.FunctionType)
assert not isinstance(type(type(type)), types.FunctionType)
