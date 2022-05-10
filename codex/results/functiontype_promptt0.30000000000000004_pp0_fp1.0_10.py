import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
assert not isinstance(lambda x: x, types.MethodType)
assert not isinstance(lambda x: x, types.LambdaType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)
assert isinstance(print, types.FunctionType)
assert not isinstance(print, types.BuiltinMethodType)
assert not isinstance(print, types.MethodType)
assert not isinstance(print, types.LambdaType)

# Test types.BuiltinMethodType
assert is
