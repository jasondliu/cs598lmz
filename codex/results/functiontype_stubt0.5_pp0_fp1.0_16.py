from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
c = {'a': 1, 'b': 2}
d = {1, 2, 3}
e = 'abc'
f = b'abc'
g = range(10)
h = FunctionType(lambda x: x, lambda: None)()
i = 1
j = 1.1
k = None
l = True

print(a, b, c, d, e, f, g, h, i, j, k, l)
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h), type(i), type(j), type(k), type(l))
print(isinstance(a, Iterator), isinstance(b, Iterable), isinstance(c, Iterable), isinstance(d, Iterable), isinstance(e, Iterable), isinstance(f, Iterable), isinstance(g, Iterable), isinstance(h, Iterable), isinstance(i, Iterable), isinstance(j, Iterable), isinstance(k,
