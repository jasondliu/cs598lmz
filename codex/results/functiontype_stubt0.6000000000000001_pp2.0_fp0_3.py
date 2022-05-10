from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))
print(isinstance(a, FunctionType))
print(isinstance(a, type))
print(isinstance(a, object))

b = [1, 2, 3]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, IteratorType))
print(isinstance(b, IterableType))
print(isinstance(b, FunctionType))
print(isinstance(b, type))
print(isinstance(b, object))

c = {'a': 1}
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, IteratorType))
print(isinstance(c, IterableType))
print(isinstance(c, FunctionType))
print(isinstance(c, type))
print(isinstance(c, object))

d = range(10)
print(type(d))
