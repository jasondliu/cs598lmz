from types import FunctionType
a = (x for x in [1])
b = [1]
c = FunctionType
print(type(a))
print(type(b))
print(type(c))


d = isinstance([], list)
e = isinstance(type, type)
f = isinstance(FunctionType, type)
print(d, e, f)

g = type(type)
h = type([])
i = type(FunctionType)
print(g, h, i)

j = type(type) is type
k = type([]) is type
m = type(FunctionType) is type
print(j, k, m)

n = type(type) is type
o = type([]) is type
p = type(FunctionType) is type
print(n, o, p)

q = type(type) == type
r = type([]) == list
s = type(FunctionType) == type
print(q, r, s)

t = [1, 2, 3]
u = (1, 2, 3)
v = {'A', 'B', 'C'}
x = {1,
