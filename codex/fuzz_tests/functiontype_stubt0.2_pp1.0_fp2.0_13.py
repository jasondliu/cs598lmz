from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)

print(a.__next__())
print(a.__next__())

b = [1, 2, 3]
print(type(b.__iter__))
print(type(b.__iter__) == FunctionType)
print(type(b.__next__))
print(type(b.__next__) == FunctionType)

c = iter(b)
print(type(c))
print(type(c.__iter__))
print(type(c.__iter__) == FunctionType)
print(type(c.__next__))
print(type(c.__next__) == FunctionType)

print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())
