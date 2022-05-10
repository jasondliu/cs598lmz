from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, IteratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))

b = [x for x in [2]]
print(isinstance(b, GeneratorType))
print(isinstance(b, IteratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, Iterable))
print(isinstance(b, Iterator))

c = (x for x in [3])
d = iter(c)
print(isinstance(d, GeneratorType))
print(isinstance(d, IteratorType))
print(isinstance(d, FunctionType))
print(isinstance(d, Iterable))
print(isinstance(d, Iterator))

e = iter(c)
print(isinstance(e, GeneratorType))
print(isinstance(e, IteratorType))
print(isinstance(e, FunctionType))
print(isinstance(e, Iterable))
print(
