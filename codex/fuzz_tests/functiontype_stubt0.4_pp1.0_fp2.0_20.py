from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = a.__iter__()
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

print(next(b))
print(next(b))
