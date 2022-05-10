from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)
print(next(a))
# print(next(a))
