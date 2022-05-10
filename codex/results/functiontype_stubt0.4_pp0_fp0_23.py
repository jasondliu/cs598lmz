from types import FunctionType
a = (x for x in [1])
b = lambda x:x
print(type(a))
print(type(b))
print(type(b) == FunctionType)

print(isinstance(b, FunctionType))

print(isinstance(a, GeneratorType))
