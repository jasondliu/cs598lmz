import types
# Test types.FunctionType
def f(): pass
def g(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(g, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(g, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(g, types.LambdaType)

# Test types.BuiltinFunctionType
def f(): pass
def g(): pass
assert not isinstance(f, types.FunctionType)
assert not isinstance(g, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(g, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(g, types.BuiltinMethodType)

