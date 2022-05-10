from types import FunctionType
a = (x for x in [1])
b = (x for x in range(2))

print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(isinstance(a, list))
print(isinstance(b, list))
