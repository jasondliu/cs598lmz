import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
assert not isinstance(None, types.BuiltinMethodType)
assert not isinstance(lambda x: x, types.MethodType)
assert not isinstance(None, types.MethodType)
