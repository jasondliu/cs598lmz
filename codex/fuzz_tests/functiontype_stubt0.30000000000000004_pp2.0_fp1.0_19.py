from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a, globals())
print(type(b))

c = b()
print(type(c))

d = next(c)
print(d)

e = next(c)
print(e)

f = next(c)
print(f)

g = next(c)
print(g)

h = next(c)
print(h)

i = next(c)
print(i)
