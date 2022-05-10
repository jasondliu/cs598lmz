import types
# Test types.FunctionType
def foo():
    pass

print(type(foo) == types.FunctionType)
print(type(foo) == types.BuiltinFunctionType)
print(type(len) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.LambdaType
print(type(lambda x: x) == types.LambdaType)

# Test types.GeneratorType
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MappingProxyType
d = {1: 'A'}
print(type(d) == types.MappingProxyType)
print(type(d) == types.DictProxyType)

# Test types.SimpleNamespace
print(type(types.SimpleNamespace()) == types.SimpleNamespace)

# Test types.MappingProxyType
d = {1: 'A'}
print(type(d) == types.Mapping
