from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(type(a))
print(type(b))
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = [1,2]
b = [1,2]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = {'a': 1, 'b': 2}
b = {'a': 1, 'b': 2}
print(a == b)
print(a is b)
print(id(a))
print(id(b))

a = {1, 2, 3}
b = {1, 2, 3}
print(a == b)
print(a is b)
print(id(a))
print(id(b))
