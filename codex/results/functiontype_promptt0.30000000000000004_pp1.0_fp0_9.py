import types
# Test types.FunctionType
def f(): pass

assert isinstance(f, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(1.0, types.FunctionType)
assert not isinstance('1', types.FunctionType)
assert not isinstance(lambda x: x, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(1.0, types.BuiltinFunctionType)
assert not isinstance('1', types.BuiltinFunctionType)
assert not isinstance(lambda x: x, types.BuiltinFunctionType)
assert not isinstance(f, types.GeneratorType)
assert not isinstance(1, types.GeneratorType)
assert not isinstance(1.0, types.GeneratorType)
assert not isinstance('1', types.GeneratorType)
assert not isinstance(lambda x: x, types.GeneratorType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(1, types.
