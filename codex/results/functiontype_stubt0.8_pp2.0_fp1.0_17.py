from types import FunctionType
a = (x for x in [1])
b = a.__iter__()
c = iter(a)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(next(a))
print(next(a))
# print(b.__next__())
# print(b.__next__())

print(type(a.__iter__()) == FunctionType)
