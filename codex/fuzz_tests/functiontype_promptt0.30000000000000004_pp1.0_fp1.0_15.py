import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(3, types.FunctionType)
assert not isinstance("abc", types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(3, types.BuiltinFunctionType)
assert not isinstance("abc", types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(3, types.BuiltinFunctionType)
assert not isinstance("abc", types.BuiltinFunctionType)

# Test types.LambdaType
assert not isinstance(f, types.
