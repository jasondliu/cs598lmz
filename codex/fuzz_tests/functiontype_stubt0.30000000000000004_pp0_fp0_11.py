from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))
print(isinstance(b, list))

c = {x for x in [1]}
print(type(c))
print(isinstance(c, GeneratorType))
print(isinstance(c, FunctionType))
print(isinstance(c, list))

d = {x: x for x in [1]}
print(type(d))
print(isinstance(d, GeneratorType))
print(isinstance(d, FunctionType))
print(isinstance(d, list))

e = lambda x: x
print(type(e))
print(isinstance(e, GeneratorType))
print(isinstance(e, FunctionType))
print(isinstance(e, list))

f = [x for x in [1] if x
