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

e = set([1])
print(e)
print(type(e))

f = set()
print(f)
print(type(f))

g = FunctionType(lambda x:x, globals())
print(g)
print(type(g))

h = (x for x in [1])
print(h)
print(type(h))

i = (x for x in [1])
print(i)
print(type(i))

j = (x for x in [1])
print(j)
print(type(j))

k = (x for x in [1])
print(k)
print(type(k))

l = (x for x
