from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(a is b)
print(type(a))
print(type(b))

print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(a.__class__)
print(b.__class__)

print(a.__class__ == b.__class__)

print(a.__class__ is b.__class__)
