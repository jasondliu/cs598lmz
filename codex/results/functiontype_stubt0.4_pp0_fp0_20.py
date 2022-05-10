from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(type(a) == type(b))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print(a.__class__)
print(a.__class__.__class__)
print(a.__class__.__class__.__class__)

print(a.__class__.__class__.__class__.__class__)
print(a.__class__.__class__.__class__.__class__.__class__)
print(a.__class__.__class__.__class__.__class__.__class__.__class__)

print(a.__class__.__class__.__class__.__class__.__class__.__class__.__class__)
print(a.__class__.__class__.__class__.__class__.__class__.__class__.__class__.__class__)
print(a.__class__.__class__.__class__
