from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = [x for x in [1] if x]
d = {x: x for x in [1]}
e = {x for x in [1]}
f = {x: x for x in [1] if x}
g = {x for x in [1] if x}
h = []
i = {}
j = set()
k = FunctionType(lambda x: x, globals())
l = lambda x: x
m = (x for x in [1] if x)
n = {x: x for x in [1] if x}
o = {x for x in [1] if x}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(n
