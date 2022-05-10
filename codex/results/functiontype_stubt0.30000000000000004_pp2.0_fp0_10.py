from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(isinstance(a, (GeneratorType, FunctionType)))

print(type(a) == type(print))
print(type(a) == type(lambda x: x))
print(type(a) == types.GeneratorType)
print(type(a) == types.FunctionType)

print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

print(isinstance(a, (types.GeneratorType, types.FunctionType)))

print(type(a) == types.GeneratorType)
print(type(a) == types.FunctionType)

print(isinstance(a, types.GeneratorType))
print(isinstance(a, types.FunctionType))

print(isinstance(a, (types.GeneratorType, types.FunctionType)))
