from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))

# print(type(a.__iter__))
print(type(a.__iter__) == FunctionType)
print(type(a.__iter__) == type(a.__next__))

print(a.__iter__)
print(a.__next__)

print(a.__iter__() is a)
print(a.__next__() == 1)

b = [1, 2, 3]
c = b.__iter__()
print(c is b)
print(c.__next__() == 1)
print(c.__next__() == 2)
print(c.__next__() == 3)

d = b.__iter__()
print(d.__next__())
print(d.__next__())
print(d.__next__())

e = (x for x in [1, 2, 3])
print(e.__next__())
print(e.__next__())
print(e.__next__())


