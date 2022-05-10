from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, list))
print(isinstance(b, list))

a = {1, 2, 3}
b = {1, 2, 3}
print(a == b)
print(a is b)
print(type(a))
print(type(b))
print(type(a
