from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a == b)
print(a is b)
print(type(a))
print(type(a) is GeneratorType)
print(type(a) is FunctionType)
