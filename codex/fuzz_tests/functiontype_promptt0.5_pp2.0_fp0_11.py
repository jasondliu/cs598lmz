import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
assert not isinstance(lambda x: x, types.MethodType)
assert not isinstance(lambda x: x, types.LambdaType)

def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
assert not isinstance(lambda x: x, types.MethodType)
assert isinstance(lambda x: x, types.Lambda
