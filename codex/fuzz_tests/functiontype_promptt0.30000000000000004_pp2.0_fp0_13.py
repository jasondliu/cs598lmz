import types
# Test types.FunctionType
def func(x):
    return x
assert isinstance(func, types.FunctionType)
assert not isinstance(func, types.BuiltinFunctionType)
assert not isinstance(func, types.BuiltinMethodType)
assert not isinstance(func, types.MethodType)
assert not isinstance(func, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.LambdaType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert not isinstance(list.append, types.FunctionType)
assert not isinstance(list.append, types.BuiltinFunctionType)
assert not isinstance(list.append, types.MethodType)
assert not isinstance(list.append, types.LambdaType)

# Test types
