import types
# Test types.FunctionType

def f(x):
    return x

assert isinstance(f, types.FunctionType)
assert isinstance(lambda x: x, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(lambda x: x, types.BuiltinMethodType)
assert not isinstance(1, types.BuiltinMethodType)
assert not isinstance(None, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(lambda x: x, types.MethodType)
assert not isinstance(1, types.MethodType)
assert not isinstance(None, types.MethodType)
assert not isinstance(f, types
