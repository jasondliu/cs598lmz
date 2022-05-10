import types
# Test types.FunctionType
assert isinstance(id, types.FunctionType)
assert not isinstance(id, types.BuiltinFunctionType)
assert not isinstance(int, types.FunctionType)
assert not isinstance(int, types.BuiltinFunctionType)
# Test types.BuiltinFunctionType
assert not isinstance(id, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(id, types.FunctionType)
