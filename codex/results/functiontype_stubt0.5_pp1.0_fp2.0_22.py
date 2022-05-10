from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a)
print(b)
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(a == b)
print(a == a)
print(a == 1)

print(a is a)
print(a is 1)

print(a is not b)
print(a is not a)
print(a is not 1)
