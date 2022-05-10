from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
print(a)
print(type(a))
print(b)
print(type(b))

print(FunctionType)
print(type(FunctionType))

print(a.__class__)
print(b.__class__)

print(dir(a))
print(dir(b))

print(dir(a.__class__))
print(dir(b.__class__))

print(dir(type))
print(dir(type.__class__))

print(type.__class__.__class__)
print(type.__class__.__class__.__class__)
print(type.__class__.__class__.__class__.__class__)
print(type.__class__.__class__.__class__.__class__.__class__)
print(type.__class__.__class__.__class__.__class__.__class__.__class__)
print(type.__class__.__class__.__class__.__class__.__class
