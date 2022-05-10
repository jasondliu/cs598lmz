from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(b) == FunctionType)
print(type(a) is FunctionType)
print(type(b) is FunctionType)

print(type(a) == type(b) == FunctionType)
print(type(a) is type(b) is FunctionType)

print(type(a) == type(b) is FunctionType)
print(type(a) is type(b) == FunctionType)

print(type(a) == type(b) == type(lambda: None))
print(type(a) is type(b) is type(lambda: None))

print(type(a) == type(b) is type(lambda: None))
print(type(a) is type(b) == type(lambda: None))

print(
