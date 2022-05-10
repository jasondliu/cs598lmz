from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x: x for x in [1]}
d = {x for x in [1]}
e = (x for x in [1])
f = [x for x in [1]]
g = {x: x for x in [1]}
h = {x for x in [1]}
i = {x: x for x in [1]}
j = {x for x in [1]}
k = (x for x in [1])
l = [x for x in [1]]
m = {x: x for x in [1]}
n = {x for x in [1]}
o = object()
p = True
q = (1,2)

test_data = [
    (a, generator, GeneratorType),
    (b, list, ListType),
    (c, dict, DictType),
    (d, set, SetType),
    (e, generator, GeneratorType),
    (f, list, ListType),
    (g, dict, DictType),
    (h, set, Set
