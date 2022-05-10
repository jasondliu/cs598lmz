from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) is FunctionType)
print(type(b) is FunctionType)

print(type(a) == type(FunctionType))
print(type(b) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(b) is type(FunctionType))

print(type(a) == type(type(a)))
print(type(b) == type(type(b)))
print(type(a) is type(type(a)))
print(type(b) is type(type(b)))

print(type(a) == type(type(b)))
