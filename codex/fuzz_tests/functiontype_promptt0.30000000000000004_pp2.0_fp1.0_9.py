import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(lambda: None, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(lambda: None, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)

# Test types.BuiltinFunctionType
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda: None, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(list.append, types.BuiltinFunctionType)
assert not isinstance(list.append, types
