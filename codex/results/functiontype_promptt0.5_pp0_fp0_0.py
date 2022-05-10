import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)

# Test types.LambdaType
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(1, types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(1, types.GeneratorType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(chr, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance("".upper, types.BuiltinMethodType)
assert not isinstance(abs, types.BuiltinMethodType)
