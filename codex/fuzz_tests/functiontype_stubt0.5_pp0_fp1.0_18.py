from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a) is GeneratorType)

b = lambda : 1
print(type(b))
print(type(b) is FunctionType)

c = [1]
print(type(c))
print(type(c) is list)

d = {1: 1}
print(type(d))
print(type(d) is dict)

e = set([1])
print(type(e))
print(type(e) is set)

f = 1
print(type(f))
print(type(f) is int)

g = 1.0
print(type(g))
print(type(g) is float)

h = '1'
print(type(h))
print(type(h) is str)

i = b'1'
print(type(i))
print(type(i) is bytes)

j = u'1'
print(type(j))
print(type(j) is unicode)

k = True
print(type(k))
print(type
