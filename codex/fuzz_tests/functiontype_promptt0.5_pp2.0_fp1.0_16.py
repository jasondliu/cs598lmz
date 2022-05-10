import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, type(f))
assert isinstance(f, type(lambda: None))
assert issubclass(type(f), types.FunctionType)
assert issubclass(type(f), type(lambda: None))
assert issubclass(type(lambda: None), types.FunctionType)
assert issubclass(types.FunctionType, type)

# Test types.BuiltinFunctionType
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, type(f))
assert isinstance(f, type(lambda: None))
assert issubclass(type(f), types.BuiltinFunctionType)
assert issubclass(type(f), type(lambda: None))
assert issubclass(type(lambda: None), types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, type)

# Test types.GeneratorType
def g(): yield 1
g = g()
assert isinstance(g, types.GeneratorType)
assert isinstance(
