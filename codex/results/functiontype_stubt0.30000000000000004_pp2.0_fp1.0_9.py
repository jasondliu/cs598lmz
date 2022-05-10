from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

b = (x for x in [1])
print(b)
print(type(b))

c = (x for x in [1])
print(c)
print(type(c))

d = (x for x in [1])
print(d)
print(type(d))

print(type(a) == type(b))
print(type(a) == type(c))
print(type(a) == type(d))

print(type(a) is type(b))
print(type(a) is type(c))
print(type(a) is type(d))

print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))
