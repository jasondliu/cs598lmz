from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)

b = (x for x in [1])
isinstance(b, Iterator)

c = (x for x in [1])
next(c)
isinstance(c.gi_code, CodeType)

d = FunctionType(lambda x: x, globals())
isinstance(d, FunctionType)

e = (1, 2, 3)
isinstance(e, Tuple)

f = [1, 2, 3]
isinstance(f, List)

g = {1, 2, 3}
isinstance(g, Set)

h = {'a': 1, 'b': 2}
isinstance(h, Dict)

i = 1
isinstance(i, Int)

j = 1.1
isinstance(j, Float)

k = 'a'
isinstance(k, Str)

l = True
isinstance(l, bool)

m = NotImplemented
isinstance(m, NotImplementedType)

n = Ellipsis
isinstance(n,
