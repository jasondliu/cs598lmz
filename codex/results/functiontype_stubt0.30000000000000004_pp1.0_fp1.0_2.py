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

d = {x: x for x in [1]}
print(d)
print(type(d))

e = '123'
print(e)
print(type(e))

f = b'123'
print(f)
print(type(f))

g = 1
print(g)
print(type(g))

h = 1.1
print(h)
print(type(h))

i = True
print(i)
print(type(i))

j = None
print(j)
print(type(j))

k = FunctionType
print(k)
print(type(k))

l = lambda x: x
print(l)
print(type(l))

m = type
print(m)
print(type(m))

n = object
