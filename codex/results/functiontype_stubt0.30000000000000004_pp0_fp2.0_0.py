from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) == type([]))
print(type(a) is type([]))

print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))

print(type(a) == FunctionType)
print(type(a) is FunctionType)

print(type(a) == type(FunctionType()))
print(type(a) is type(FunctionType()))

print(type(a) == FunctionType())
print(type(a) is FunctionType())

print(type(a) == type(a))
print(type(a) is type(a))

print(type(a) == type(a()))
print(type(a) is type(a()))

print(type(a) == a)

