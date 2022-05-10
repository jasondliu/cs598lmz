import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(3, types.FunctionType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
assert not isinstance(3, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(3, types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(3, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert not isinstance(f, types.BuiltinMethodType)
assert not
