from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))

b = [x for x in [1]]
print(type(b))
print(isinstance(b, list))

c = {x for x in [1]}
print(type(c))
print(isinstance(c, set))

d = {x: x for x in [1]}
print(type(d))
print(isinstance(d, dict))

e = FunctionType(lambda: None, globals())
print(type(e))
print(isinstance(e, FunctionType))

f = lambda: None
print(type(f))
print(isinstance(f, FunctionType))

g = (x for x in [1])
print(type(g))
print(isinstance(g, GeneratorType))

h = [x for x in [1]]
print(type(h))
print(isinstance(h, list))

i = {x for x in [1]}
print(type(i))
print(isinstance(i, set))

j
