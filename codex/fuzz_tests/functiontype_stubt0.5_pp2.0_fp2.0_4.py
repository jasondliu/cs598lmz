from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a) == type(b))

print("-"*30)

a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a) == type(b))

print("-"*30)

a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(type(a) ==
