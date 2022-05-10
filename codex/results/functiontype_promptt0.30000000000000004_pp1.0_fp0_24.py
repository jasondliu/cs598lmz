import types
# Test types.FunctionType
def f(x):
    return x
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert not isinstance([].append, types.FunctionType)
assert not isinstance([].append, types.BuiltinFunctionType)
assert not isinstance([].append, types.MethodType)
# Test types.MethodType
def f(self):
    return self
assert isinstance(f(1), types.MethodType)
assert not isinstance(f(1), types.FunctionType)
assert not isinstance(f(1), types.
