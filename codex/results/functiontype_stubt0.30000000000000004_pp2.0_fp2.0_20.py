from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) == FunctionType)
print(isinstance(a, FunctionType))
print(isinstance(a, type(b)))
print(isinstance(a, type(a)))
print(isinstance(a, type(1)))

print(isinstance(a, type(FunctionType)))
