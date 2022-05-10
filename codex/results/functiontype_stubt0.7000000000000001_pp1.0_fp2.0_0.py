from types import FunctionType
a = (x for x in [1])
b = isinstance(a, Iterator)
c = isinstance(a, Iterable)
d = isinstance(a, Generator)
e = isinstance(a, FunctionType)
print(b, c, d, e)
