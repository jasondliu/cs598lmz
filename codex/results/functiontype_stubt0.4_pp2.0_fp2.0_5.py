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

print(a is b)
print(a is c)

print(a == b)
print(a == c)

print(a is not b)
print(a is not c)

print(a != b)
print(a != c)

print(type(a) is type(b))
print(type(a) is type(c))

print(type(a) == type(b))
print(type(a) == type(c))

print(type(a) is not type(b))
print(type(a) is not type(c))

print(type(a) != type(b))
print(type(a) != type(c))

print(type(a) is FunctionType)
print(type(a) is not FunctionType)
print(type(a)
