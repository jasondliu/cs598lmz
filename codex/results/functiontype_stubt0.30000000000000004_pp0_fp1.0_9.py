from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(a) == type(FunctionType()))
print(type(a) is type(FunctionType()))

print(type(FunctionType) == type(FunctionType()))
print(type(FunctionType) is type(FunctionType()))

print(type(FunctionType) == type(lambda x: x))
print(type(FunctionType) is type(lambda x: x))

print(type(FunctionType()) == type(lambda x: x))
print(type(FunctionType()) is type(lambda x: x))

print(type(FunctionType()) == type(FunctionType))
print(type(FunctionType()) is type(FunctionType))

print(
