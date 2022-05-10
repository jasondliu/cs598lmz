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

e = {x: x for x in [1] if x > 0}
print(e)
print(type(e))

f = {x: x for x in [1] if x > 0}
print(f)
print(type(f))

g = {x: x for x in [1] if x > 0}
print(g)
print(type(g))

h = {x: x for x in [1] if x > 0}
print(h)
print(type(h))

i = {x: x for x in [1] if x > 0}
print(i)
print(type(i))

j = {x: x for x in [1]
