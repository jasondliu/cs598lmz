import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g, types.GeneratorType)
assert isinstance(g(), types.GeneratorType)
assert not isinstance(g, types.FunctionType)
assert not isinstance(g, types.BuiltinFunctionType)
assert not isinstance(g, types.BuiltinMethodType)
assert not isinstance(g, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(map, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(map, types.FunctionType)
assert not isinstance(map, types.GeneratorType)
assert not isinstance
