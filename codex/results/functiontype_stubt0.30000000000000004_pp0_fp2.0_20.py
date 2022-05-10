from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, type(b)))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(type(a) == GeneratorType)
print(type(b) == GeneratorType)
print(type(a) is GeneratorType)
print(type(b) is GeneratorType)

print(type(a) == type(b) == GeneratorType)
print(type(a) is type(b) is GeneratorType)

print(type(a) == type(b) == GeneratorType)
print(type(a) is type(b) is GeneratorType)

print(type(a) == type(b) == GeneratorType)
print(type(a) is type(b) is GeneratorType)

print(type(a) == type(b) == GeneratorType)

