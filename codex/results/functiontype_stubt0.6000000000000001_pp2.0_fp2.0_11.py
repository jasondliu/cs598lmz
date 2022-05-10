from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

b = [1, 2]
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))

c = (x for x in [1, 2])
print(isinstance(c, Iterator))
print(isinstance(c, Iterable))

d = FunctionType
print(isinstance(d, Iterator))
print(isinstance(d, Iterable))

e = map(lambda x: x + 1, [1])
print(isinstance(e, Iterator))
print(isinstance(e, Iterable))

f = range(1)
print(isinstance(f, Iterator))
print(isinstance(f, Iterable))

g = {}
print(isinstance(g, Iterator))
print(isinstance(g, Iterable))

h = []
print(isinstance(h, Iterator))
print(isinstance(h, Iterable))

i = ''
print(is
