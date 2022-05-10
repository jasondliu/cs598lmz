from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(id(a) == id(b))

c = (x for x in [1])
d = (x for x in [1])
print(c == d)
print(id(c) == id(d))

e = (x for x in [1])
f = (x for x in [1])
print(e == f)
print(id(e) == id(f))

g = (x for x in [1])
h = (x for x in [1])
print(g == h)
print(id(g) == id(h))

i = (x for x in [1])
j = (x for x in [1])
print(i == j)
print(id(i) == id(j))

k = (x for x in [1])
l = (x for x in [1])
print(k == l)
print(id(k) == id(l))

m = (x for x in [1])
n =
