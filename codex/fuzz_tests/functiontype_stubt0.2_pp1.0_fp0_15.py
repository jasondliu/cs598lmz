from types import FunctionType
a = (x for x in [1])
print(type(a))

b = [x for x in [1]]
print(type(b))

c = {x for x in [1]}
print(type(c))

d = {x:x for x in [1]}
print(type(d))

e = FunctionType(lambda x:x, globals())
print(type(e))

f = lambda x:x
print(type(f))

g = type(x for x in [1])
print(type(g))

h = type([x for x in [1]])
print(type(h))

i = type({x for x in [1]})
print(type(i))

j = type({x:x for x in [1]})
print(type(j))

k = type(FunctionType(lambda x:x, globals()))
print(type(k))

l = type(lambda x:x)
print(type(l))

m = type(type(x for x in [1]))
print(type(m))

