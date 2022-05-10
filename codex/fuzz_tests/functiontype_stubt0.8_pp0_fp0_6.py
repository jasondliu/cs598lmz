from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = FunctionType(a, {})
print(b)
print(type(b))

c = b()
print(c)
print(type(c))

d = c()
print(d)
print(type(d))
