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

e = {x for x in [1]}.__iter__()
print(e)
print(type(e))

f = {x: x for x in [1]}.__iter__()
print(f)
print(type(f))

g = {x for x in [1]}.__iter__().__next__()
print(g)
print(type(g))

h = {x: x for x in [1]}.__iter__().__next__()
print(h)
print(type(h))

i = {x for x in [1]}.__iter__().__next__().__str__()
print(i)
print(type(i))

j =
