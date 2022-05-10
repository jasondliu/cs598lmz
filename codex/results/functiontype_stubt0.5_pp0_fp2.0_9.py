from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(isinstance(a, FunctionType))

print(a)
print(b)

print(next(a))
print(next(a))

print(next(b))
print(next(b))

print(next(a))
