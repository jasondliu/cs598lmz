from types import FunctionType
a = (x for x in [1])
b = (x for x in [1,2])
print(type(a))
print(type(b))
print(isinstance(a,FunctionType))
print(isinstance(b,FunctionType))

print(a.__next__())
print(a.__next__())

print(b.__next__())
print(b.__next__())
print(b.__next__())
