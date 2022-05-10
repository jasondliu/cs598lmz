from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])

print(a == b)
print(a is b)
print(id(a))
print(id(b))

print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) is FunctionType)
print(type(a) == FunctionType)

print(isinstance(a, FunctionType))
print(isinstance(a, type(b)))

# print(a() == b())
print(a() is b())
print(id(a()))
print(id(b()))

print(type(a()) is type(b()))
print(type(a()) == type(b()))
print(type(a()) is int)
print(type(a()) == int)

print(isinstance(a(), type(b())))
print(isinstance(a(), int))

print(a.__class__)
print(a.__class__ is b.__class__)
print(a.__class__ == b.__class__
