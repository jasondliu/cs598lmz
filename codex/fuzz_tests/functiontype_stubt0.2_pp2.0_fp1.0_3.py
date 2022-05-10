from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))

print(type(a.__iter__()) == type(a))
print(type(a.__next__()) == type(a))

print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == FunctionType)

print(a.__iter__() == a)
print(a.__next__() == a)

print(a.__iter__() is a)
print(a.__next__() is a)

print(a.__iter__() is not a)
print(a.__next__() is not a)

print(a.__iter__() is a.__next__())
print(a.__next__() is a.__iter__())

print(a.__iter__() is not a.__next__())
print(a.__next__() is not a.__iter__())

print(a.__iter__() == a.__next__())
