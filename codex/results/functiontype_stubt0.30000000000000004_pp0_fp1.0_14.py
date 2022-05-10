from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(id(a))
print(id(b))
print(a is b)
print(a.__next__())
print(a.__next__())
print(a.__next__())

print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))

print(type(a) == type(lambda x: x))
print(type(a) is type(lambda x: x))

print(type(a) == type(lambda x: x))
print(type(a) is type(lambda x: x))

print(type(a) == type(lambda x:
