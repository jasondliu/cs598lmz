from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x:x for x in [1]}
e = {x:x for x in [1] if x}
f = {x:x for x in [1] if x if x}
g = (x for x in [1] if x if x)
h = [x for x in [1] if x if x]
i = {x for x in [1] if x if x}
j = {x:x for x in [1] if x if x}
k = {x:x for x in [1] if x if x if x}
l = (x for x in [1] if x if x if x)
m = [x for x in [1] if x if x if x]
n = {x for x in [1] if x if x if x}
o = {x:x for x in [1] if x if x if x}
p = {x:x for x in [1] if x if x if x if x}
q = (
