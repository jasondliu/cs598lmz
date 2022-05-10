from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(type(a))
print(type(b))
print(a.__iter__() == b.__iter__())
print(a.__iter__() is b.__iter__())
print(a.__next__() == b.__next__())
print(a.__next__() is b.__next__())
print(a.__next__() is a.__next__())
print(a.__next__() is b.__next__())
print(a.__next__() is a.__next__())
print(a.__next__() is b.__next__())

print('\n-----------\n')

c = [1]
d = [2]
print(type(c))
print(type(d))
print(c.__iter__() == d.__iter__())
print(c.__iter__() is d.__iter__())
print(c.__getitem__(0) == d.__getitem__(0))
print(c.__getitem__(0
