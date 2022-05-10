from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))
print(isinstance(a, IterableType))

b = [1, 2]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, IteratorType))
print(isinstance(b, IterableType))

c = {1: 2}
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, IteratorType))
print(isinstance(c, IterableType))

d = {1, 2}
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))
print(isinstance(d, IteratorType))
print(isinstance(d, IterableType))

e = 'abc'
print(type(e))
print
