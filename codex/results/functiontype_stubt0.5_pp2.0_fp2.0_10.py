from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(a)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(b) == FunctionType)

print(a.__next__())
print(a.__next__())

print(b.__next__())
print(b.__next__())
