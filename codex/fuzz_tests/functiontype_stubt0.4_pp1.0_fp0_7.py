from types import FunctionType
a = (x for x in [1])
print(type(a))
b = (x for x in [1])
print(type(b))
print(a == b)
print(a is b)

def f(x):
    return x

print(type(f))
print(type(FunctionType))
print(f == FunctionType)
print(f is FunctionType)

print(type(f) == FunctionType)
print(type(f) is FunctionType)

print(type(f) == type(FunctionType))
print(type(f) is type(FunctionType))

print(type(f) == type(f))
print(type(f) is type(f))

print(type(FunctionType) == type(FunctionType))
print(type(FunctionType) is type(FunctionType))

print(type(FunctionType) == type(type))
print(type(FunctionType) is type(type))

print(type(type) == type(type))
print(type(type) is type(type))

print(type(type) == type(FunctionType))
print(
