from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)

print(type(a))
print(type(b))
print(type(a) == type(b))

print(type(a) == FunctionType)
print(type(b) == FunctionType)

print(type(a) == GeneratorType)
print(type(b) == GeneratorType)
