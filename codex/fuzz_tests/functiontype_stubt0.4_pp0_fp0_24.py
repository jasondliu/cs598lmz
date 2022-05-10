from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))

b = [1, 2, 3]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, FunctionType))

c = (x for x in [1, 2, 3])
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))
print(isinstance(c, FunctionType))

d = map(lambda x: x, [1, 2, 3])
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, Iterator))
print(isinstance(d, Iterable))
print(isinstance(d, FunctionType))

e = filter(
