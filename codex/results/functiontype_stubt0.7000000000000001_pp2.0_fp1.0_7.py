from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = (x for x in [1])
print(isinstance(b, Iterable))

c = (x for x in [1])
print(isinstance(c, Iterator))

d = (x for x in [1])
print(isinstance(d, FunctionType))

e = (x for x in [1])
print(isinstance(e, list))

f = (x for x in [1])
print(isinstance(f, tuple))

g = (x for x in [1])
print(isinstance(g, dict))

h = (x for x in [1])
print(isinstance(h, set))

i = (x for x in [1])
print(isinstance(i, frozenset))

j = (x for x in [1])
print(isinstance(j, str))

print('\n')

print(isinstance(a, str))
print(isinstance(a, object))
print(isinstance(a, int))

#
