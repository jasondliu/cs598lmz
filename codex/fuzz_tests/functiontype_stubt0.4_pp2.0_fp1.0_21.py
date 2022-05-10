from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) is FunctionType)
print(type(b) is FunctionType)
print(type(a) == FunctionType)
print(type(b) == FunctionType)

print(type(a) is GeneratorType)
print(type(b) is GeneratorType)
print(type(a) == GeneratorType)
print(type(b) == GeneratorType)

print(type(a) is Iterator)
print(type(b) is Iterator)
print(type(a) == Iterator)
print(type(b) == Iterator)

print(type(a) is Iterable)
print(type(b) is Iterable)
print(type(a) == Iterable)
print(type(b) == Iterable)

print(type(a) is object)
print(type(b) is object)
print(type(a
