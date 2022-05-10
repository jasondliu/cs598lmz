import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(f, types.GeneratorType)

# Test types.BuiltinFunctionType
def g():
    pass
assert isinstance(g, types.FunctionType)
assert isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(g, types.MethodType)
assert not isinstance(g, types.LambdaType)
assert not isinstance(g, types.GeneratorType)

# Test types.BuiltinMethodType
assert isinstance(str.upper, types.FunctionType)
assert not isinstance(str.upper, types.BuiltinFunctionType)
assert isinstance(str.upper, types.BuiltinMethodType)
assert not isinstance(str.
