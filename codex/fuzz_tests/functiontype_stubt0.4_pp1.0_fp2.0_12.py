from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a) is type(b))
print(FunctionType is type(a))
print(type(a) is FunctionType)
print(type(a) == FunctionType)
print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a) is type(a))

print(type(a) is type(a))
print(type(a
