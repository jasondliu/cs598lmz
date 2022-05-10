import types
# Test types.FunctionType

def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance(3.14, types.FunctionType)
assert not isinstance("abc", types.FunctionType)
assert not isinstance(b"abc", types.FunctionType)
assert not isinstance(bytearray(b"abc"), types.FunctionType)
assert not isinstance(u"abc", types.FunctionType)
assert not isinstance([], types.FunctionType)
assert not isinstance((), types.FunctionType)
assert not isinstance({}, types.FunctionType)
assert not isinstance(object(), types.FunctionType)
assert not isinstance(object, types.FunctionType)

# Test types.LambdaType

assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
