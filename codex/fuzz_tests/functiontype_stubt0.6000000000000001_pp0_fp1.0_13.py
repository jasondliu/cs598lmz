from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2, 3])
c = (x for x in [1, 2, 3, 4, 5, 6])

print(type(a))
print(type(b))
print(type(c))

print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, GeneratorType))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(isinstance(c, FunctionType))

print(isinstance(a, Iterator))
print(isinstance(b, Iterator))
print(isinstance(c, Iterator))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))

print(isinstance(a, Sequence))
print(isinstance(b, Sequence))
print(isinstance(c, Sequence))

print(isinstance(a, Container))
print(isinstance(b, Container))
print(isinstance(c, Container
