import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert isinstance(object, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(object, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert not isinstance(lambda: None, types.BuiltinMethodType)
assert isinstance(int, types.BuiltinMethodType)
assert not isinstance(object, types.BuiltinMethodType)
assert not isinstance(1, types.BuiltinMethodType)
assert not isinstance
