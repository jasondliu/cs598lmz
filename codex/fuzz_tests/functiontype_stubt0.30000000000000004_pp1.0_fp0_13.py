from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == type(x for x in [1]))
print(type(a) is type(x for x in [1]))
print(type(a) == type(lambda x: x))
print(type(a) is type(lambda x: x))
print(type(a) == FunctionType)
print(type(a) is FunctionType)

print(type(a) == type(b) == type(x for x in [1]) == type(lambda x: x) == FunctionType)
print(type(a) is type(b) is type(x for x in [1]) is type(lambda x: x) is FunctionType)

print(type(a) == type(b) == type(x for x in [1]) == type(lambda x: x) == type(Function
