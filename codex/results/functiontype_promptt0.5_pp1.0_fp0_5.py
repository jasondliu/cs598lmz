import types
# Test types.FunctionType

def f(x):
    return x

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType

assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.BuiltinMethodType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(abs, types.LambdaType)
assert not isinstance(abs, types.FunctionType)

# Test types.BuiltinMethodType

assert isinstance("".replace, types.BuiltinMethodType)
assert not isinstance("".replace, types.MethodType)
assert not isinstance("".replace, types.LambdaType)
assert not isinstance("".replace, types.FunctionType)
assert not isinstance("".replace, types.BuiltinFunctionType)

# Test types.
