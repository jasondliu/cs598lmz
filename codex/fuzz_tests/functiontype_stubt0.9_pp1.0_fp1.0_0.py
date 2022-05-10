from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a) == type(b))
print(type(a) == GeneratorType)
print(type(b) == GeneratorType)
print(type(a) is GeneratorType)
print(type(b) is GeneratorType)
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

a = FunctionType('lambda')
a = lambda x:x
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(isinstance(a, FunctionType))
