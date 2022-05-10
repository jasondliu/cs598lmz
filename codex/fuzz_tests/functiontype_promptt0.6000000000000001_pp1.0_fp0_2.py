import types
# Test types.FunctionType
def f():
    pass
f2 = lambda x: x
f3 = f
assert isinstance(f, types.FunctionType)
assert isinstance(f2, types.FunctionType)
assert isinstance(f3, types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(f2, types.LambdaType)
assert not isinstance(f3, types.LambdaType)
assert isinstance(lambda x: x, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f2, types.BuiltinFunctionType)
assert not isinstance(f3, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append,
