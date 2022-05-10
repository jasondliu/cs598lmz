import types
# Test types.FunctionType

def f(): pass

assert isinstance(f, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType

assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(1, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
assert not isinstance(object, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.GeneratorType

def g(): yield 1

assert isinstance(g(), types.GeneratorType)
assert not isinstance(1, types.GeneratorType)
assert not isinstance(None, types.GeneratorType)
assert not isinstance(object, types.GeneratorType)
assert not isinstance(f, types.GeneratorType)

# Test types.CodeType

assert
