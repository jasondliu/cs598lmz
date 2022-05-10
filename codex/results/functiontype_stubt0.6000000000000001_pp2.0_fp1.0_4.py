from types import FunctionType
a = (x for x in [1])
b = ([x for x in [1]],)
c = {x for x in [1]}
d = {'a': x for x in [1]}
e = {x: x for x in [1]}
f = FunctionType()
g = list.append
h = zip([1], [2])
i = range(1)
j = {1}
k = (1, 2)
l = 1

print(isinstance(a, collections.Iterable))
print(isinstance(b, collections.Iterable))
print(isinstance(c, collections.Iterable))
print(isinstance(d, collections.Iterable))
print(isinstance(e, collections.Iterable))
print(isinstance(f, collections.Iterable))
print(isinstance(g, collections.Iterable))
print(isinstance(h, collections.Iterable))
print(isinstance(i, collections.Iterable))
print(isinstance(j, collections.Iterable))
print(isinstance(k, collections.Iterable))
print(isinstance(l, collections.Iterable))
