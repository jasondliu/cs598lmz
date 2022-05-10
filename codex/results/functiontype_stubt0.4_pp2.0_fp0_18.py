from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(a.__next__())
print(a.__next__())

print(type(a) == type(b))
print(type(a) == FunctionType)

print(callable(a))
print(callable(b))
print(callable(a.__next__))
print(callable(b.__next__))

print(callable(a.__next__()))
print(callable(b.__next__()))
