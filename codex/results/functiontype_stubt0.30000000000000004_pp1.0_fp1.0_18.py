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

print(a.__iter__())
print(a.__iter__())

b = (x for x in [1, 2])
print(b.__next__())
print(b.__next__())
print(b.__next__())

print(a.__next__())
print(a.__next__())

print(b.__next__())
print(b.__next__())

print(a.__next__())
print(a.__next__())

print(b.__next__())
print(b.__next__())

print(a.__next__())
print(a.__next__())


