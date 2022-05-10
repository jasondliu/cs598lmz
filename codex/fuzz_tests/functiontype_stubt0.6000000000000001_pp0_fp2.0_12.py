from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a)
print(b)
print(a == b)
print(a is b)
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(issubclass(GeneratorType, Iterator))
print(issubclass(GeneratorType, Iterable))
print(issubclass(GeneratorType, FunctionType))
