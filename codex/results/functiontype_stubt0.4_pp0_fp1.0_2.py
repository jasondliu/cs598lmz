from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])
d = (x for x in [1])

print(a)
print(b)
print(c)
print(d)

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print(a == b)
print(b == c)
print(c == d)
print(d == a)

print(type(a) == type(b))
print(type(b) == type(c))
print(type(c) == type(d))
print(type(d) == type(a))

print(type(a) is type(b))
print(type(b) is type(c))
print(type(c) is type(d))
print(type(d) is type(a))

print(type(a) == type(FunctionType))
print(type(b) == type(FunctionType))
print(type(c) == type(FunctionType))
print(type(
