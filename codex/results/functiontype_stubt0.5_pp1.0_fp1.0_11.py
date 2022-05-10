from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(a)
print(b)

print(FunctionType)

a = 1
b = 1
print(a == b)
print(a is b)
print(a)
print(b)
