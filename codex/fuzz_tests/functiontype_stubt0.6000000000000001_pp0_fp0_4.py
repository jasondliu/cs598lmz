from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = [x for x in range(10)]
print(isinstance(b, list))

c = map(lambda x: x, range(10))
print(isinstance(c, map))

d = filter(lambda x: x, range(10))
print(isinstance(d, filter))

e = FunctionType(lambda x: x, globals())
print(isinstance(e, FunctionType))

f = lambda x: x
print(isinstance(f, FunctionType))

g = 100
print(isinstance(g, int))

print(isinstance(g, tuple))

h = (1, 2)
print(isinstance(h, tuple))

i = []
print(isinstance(i, list))

j = {}
print(isinstance(j, dict))
