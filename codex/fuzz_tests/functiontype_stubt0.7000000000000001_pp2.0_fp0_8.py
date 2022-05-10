from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda a: a))
print(type(FunctionType))
print(type(hasattr))

print("-" * 20)
# all object has a __class__ attribute
print(a.__class__)
print(FunctionType.__class__)

print("-" * 20)
# __class__ is a attribute of an object
print(a.__class__.__class__)
print(FunctionType.__class__.__class__)

print("-" * 20)
# __class__ is a type object
print(type(a.__class__))
print(type(FunctionType.__class__))

print("-" * 20)
# type is a type object
print(type(type))

print("-" * 20)
# type is a type object
print(type(type))

# type(type) == type
print(type(type) == type)

print("-" * 20)
# type is a type object
print(type(type))
print(type(type).__class__)
