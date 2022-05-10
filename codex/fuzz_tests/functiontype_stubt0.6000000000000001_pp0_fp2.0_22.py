from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])

print(type(a))
print(type(b))
print(type(c))

print(type(a) == type(b))
print(type(a) == type(c))
print(type(b) == type(c))

print(a == b)
print(a == c)
print(b == c)

print(type(a) == FunctionType)
