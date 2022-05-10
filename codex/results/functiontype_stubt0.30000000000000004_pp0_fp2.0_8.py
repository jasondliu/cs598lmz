from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, GeneratorType))

c = FunctionType(lambda x: x, lambda: None)
print(type(c))
print(isinstance(c, GeneratorType))

d = (x for x in [1])
print(type(d))
print(isinstance(d, GeneratorType))

e = (x for x in [1])
print(type(e))
print(isinstance(e, GeneratorType))

f = (x for x in [1])
print(type(f))
print(isinstance(f, GeneratorType))

g = (x for x in [1])
print(type(g))
print(isinstance(g, GeneratorType))

h = (x for x in [1])
print(type(h))
print(isinstance(h, GeneratorType))

i = (x for x in [1])
print(type(i))
print(is
