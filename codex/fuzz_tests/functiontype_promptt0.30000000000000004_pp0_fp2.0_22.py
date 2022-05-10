import types
# Test types.FunctionType
def f():
    pass
def g():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(g, types.MethodType)
assert not isinstance(f, types.UnboundMethodType)
assert not isinstance(g, types.UnboundMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(max, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(min, types.FunctionType)
assert not isinstance(max, types.FunctionType)
assert not isinstance(len, types.
