from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda x: x, globals())
f = type(lambda x: x)
g = type(x for x in [1])
h = type([x for x in [1]])
i = type({x for x in [1]})
j = type({x: x for x in [1]})
k = type(FunctionType(lambda x: x, globals()))
l = type(type(lambda x: x))
m = type(type(x for x in [1]))
n = type(type([x for x in [1]]))
o = type(type({x for x in [1]}))
p = type(type({x: x for x in [1]}))
q = type(type(FunctionType(lambda x: x, globals())))
print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o,
