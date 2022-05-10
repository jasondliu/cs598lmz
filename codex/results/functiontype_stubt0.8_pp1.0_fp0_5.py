from types import FunctionType
a = (x for x in [1])
type(a)

b = (1 for x in [1])
type(b)

c = (x for x in [1] if x == 1)
type(c)

d = FunctionType(lambda x: x, [])
type(d)

e = FunctionType(lambda x: x, [1])
type(e)

f = FunctionType(lambda x: x, [1, 2])
type(f)

g = FunctionType(lambda x: x, [1, 2], {})
type(g)

h = FunctionType(lambda x: x, [1, 2], {}, None)
type(h)

i = FunctionType((lambda x: x), [1, 2], {}, None)
type(i)

j = FunctionType(lambda x: x, (1, 2), {}, None)
type(j)

k = FunctionType(lambda x: x, (1, 2), {}, None, None)
type(k)
