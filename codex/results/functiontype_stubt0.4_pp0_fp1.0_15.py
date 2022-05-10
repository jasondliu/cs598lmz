from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) == GeneratorType)
print(type(a) is GeneratorType)

print(type(a) == FunctionType)
print(type(a) is FunctionType)
