import types
# Test types.FunctionType is a class
assert isinstance(types.FunctionType, type)
def foo(): pass
assert isinstance(foo, types.FunctionType)
assert isinstance(foo, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType is a class
assert isinstance(types.BuiltinFunctionType, type)

# Test types.MethodType is a class
assert isinstance(types.MethodType, type)

# Test types.GeneratorType is a class
assert isinstance(types.GeneratorType, type)

# Test types.CoroutineType is a class
assert isinstance(types.CoroutineType, type)

# Test types.AsyncGeneratorType is a class
assert isinstance(types.AsyncGeneratorType, type)

# Test types.SimpleNamespace is a class
assert isinstance(types.SimpleNamespace, type)

# Test types.MappingProxyType is a class
assert isinstance(types.MappingProxyType, type)

# Test types.ChainMap is a class
assert isinstance(types.ChainMap, type)

# Test types.Tr
