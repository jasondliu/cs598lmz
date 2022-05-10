from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(type(a) == types.GeneratorType)
print(type(a) == types.FunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

print(isinstance(a, (GeneratorType, FunctionType)))
print(isinstance(a, (types.GeneratorType, types.FunctionType)))

print(isinstance(a, (GeneratorType, FunctionType, int)))
print(isinstance(a, (types.GeneratorType, types.FunctionType, int)))

print(isinstance(a, (GeneratorType, FunctionType, int, str)))
print(isinstance(a, (types.GeneratorType, types.FunctionType, int, str)))

print(isinstance(a, (GeneratorType, FunctionType, int, str, list)))

