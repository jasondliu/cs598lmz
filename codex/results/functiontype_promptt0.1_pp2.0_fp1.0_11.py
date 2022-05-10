import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(lambda: None, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(lambda: None, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert isinstance([].append, types.MethodType)
assert isinstance([].append, types.BuiltinFunctionType)
assert isinstance([].append, types.FunctionType)


