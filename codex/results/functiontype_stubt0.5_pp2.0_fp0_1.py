from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)

a = (x for x in [1, 2])
b = (x for x in [1, 2])
print(a == b)

a = (x for x in [1, 2])
b = (x for x in [1, 2, 3])
print(a == b)

a = (x for x in [1, 2, 3])
b = (x for x in [1, 2, 3])
print(a == b)

a = (x for x in [1])
b = (x for x in [1, 2])
print(a == b)

a = (x for x in [1, 2])
b = (x for x in [1])
print(a == b)

print(FunctionType)
print(type(FunctionType))
