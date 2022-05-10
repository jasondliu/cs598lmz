from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == type(FunctionType))
print(type(a) is type(FunctionType))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(FunctionType))
print(type(FunctionType) == type(FunctionType))
print(type(FunctionType) is type(FunctionType))
print(type(FunctionType) == FunctionType)
print(type(FunctionType) is FunctionType)
print(FunctionType)
print(FunctionType == FunctionType)
print(FunctionType is FunctionType)

print('\n\n')

class A:
    pass

class B:
    pass

a = A()
b = A()
print(a == b)
print(a is b)
print(type(a))
print(
