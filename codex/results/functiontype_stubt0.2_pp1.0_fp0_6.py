from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(a.__next__())
print(a.__next__())
print(a.__next__())

print(a.__iter__())
print(a.__iter__())
print(a.__iter__())

b = [1, 2, 3]
print(type(b))
print(type(b.__iter__))
print(type(b.__iter__) == FunctionType)
print(type(b.__iter__()) == type(b))
print(type(b.__iter__()) == type(b.__iter__()))
print(type(b.__iter__()) == type(b.__iter__()))
print(type(b.__iter__()) == type(b.__iter
