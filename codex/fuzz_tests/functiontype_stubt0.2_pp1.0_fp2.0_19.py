from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(FunctionType == FunctionType)
print(FunctionType is FunctionType)
print(type(FunctionType) == type(FunctionType))
print(type(FunctionType) is type(FunctionType))

print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))

print(type(a) == type(b))
print(type(a) is type(b))

print(type(a) == type(type(a)))
print(type(a) is type(type(a)))

print(type(a) == type(type(b)))
print(type(a) is type(type(b)))

print(type(a) == type(type(FunctionType)))
print(type(a) is type(type(FunctionType)))

print(type(a) == type(type(type(a))))
print
