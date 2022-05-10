from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))
print(isinstance(a, GeneratorType))

b = print
print(type(b))
print(isinstance(b, FunctionType))

c = [x for x in [1]]
print(type(c))
print(isinstance(c, FunctionType))

d = {x for x in [1]}
print(type(d))
print(isinstance(d, FunctionType))
