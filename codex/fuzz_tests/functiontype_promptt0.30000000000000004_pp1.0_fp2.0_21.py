import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(types, types.FunctionType)
assert not isinstance(types.FunctionType, types.FunctionType)
assert not isinstance(types.FunctionType.__call__, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(object.__init__, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(object, types.BuiltinFunctionType)
assert not isinstance(type, types.BuiltinFunctionType)
assert not isinstance(types, types.BuiltinFunctionType)
