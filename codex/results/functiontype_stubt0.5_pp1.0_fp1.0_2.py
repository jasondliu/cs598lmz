from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(type(a))
print(type(b))
c = [x for x in [1] if x > 0]
print(type(c))
d = [x for x in [1] if x > 0 else 0]
print(type(d))
e = [x for x in [1] if x > 0 else x for x in [1]]
print(type(e))
f = [x for x in [1] if x > 0 else x for x in [1] if x > 0]
print(type(f))
g = [x for x in [1] if x > 0 else x for x in [1] if x > 0 else 0]
print(type(g))
h = [x for x in [1] if x > 0 else x for x in [1] if x > 0 else 0 if x > 0 else 0]
print(type(h))
i = [x for x in [1] if x > 0 else x for x in [1] if x > 0 else 0 if x > 0 else 0 if x
