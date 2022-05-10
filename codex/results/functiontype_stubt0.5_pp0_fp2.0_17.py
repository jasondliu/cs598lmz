from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
b = [x for x in [1]]
print(b)
print(type(b))
c = {x for x in [1]}
print(c)
print(type(c))
d = {x:x for x in [1]}
print(d)
print(type(d))
e = FunctionType(lambda x:x, globals())
print(e)
print(type(e))
f = lambda x:x
print(f)
print(type(f))
g = (x for x in [1])
print(g)
print(type(g))
h = [x for x in [1]]
print(h)
print(type(h))
i = {x for x in [1]}
print(i)
print(type(i))
j = {x:x for x in [1]}
print(j)
print(type(j))
k = FunctionType(lambda x:x, globals())
print(k)
print(type(k))
l = lambda x:x
