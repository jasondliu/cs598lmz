from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, IteratorType))

print(isinstance(a, IterableType))

b = [1,2,3]
print(isinstance(b, IterableType))
print(isinstance(b, IteratorType))

c = iter(b)
print(isinstance(c, IterableType))
print(isinstance(c, IteratorType))

d = (x for x in [1,2,3])
print(isinstance(d, IterableType))
print(isinstance(d, IteratorType))

e = iter(d)
print(isinstance(e, IterableType))
print(isinstance(e, IteratorType))

f = iter(e)
print(isinstance(f, IterableType))
print(isinstance(f, IteratorType))


g = iter(f)
print(isinstance(g, IterableType))
print(isinstance(g, Iterator
