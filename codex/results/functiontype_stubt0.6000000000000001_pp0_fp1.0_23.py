from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = [x for x in [1] if x]
f = [x for x in [1] if x > 1]
g = {x for x in [1] if x}
h = {x: x for x in [1] if x}
i = {x: x for x in [1] if x > 1}
j = {x: x for x in [1] if x > 1}
k = {x: x for x in [1] if x > 1 else 2}
l = {x: x for x in [1] if x > 1 else 2}
m = {x: x for x in [1] if x > 1 else 2}
n = {x: x for x in [1] if x > 1 else 2}
o = {x: x for x in [1] if x > 1 else 2}
p = {x: x for x in [1] if x > 1 else 2}
q = {
