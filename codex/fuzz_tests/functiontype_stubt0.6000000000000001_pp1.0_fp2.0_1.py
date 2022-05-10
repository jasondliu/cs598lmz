from types import FunctionType
a = (x for x in [1])

type(a)

b = [x for x in [1]]

type(b)

c = {x for x in [1]}

type(c)

d = {x: x for x in [1]}

type(d)

e = {x for x in [1] if x > 0}

type(e)

f = {x: x for x in [1] if x > 0}

type(f)

g = {x for x in [1] for y in [2]}

type(g)

h = {x: x for x in [1] for y in [2]}

type(h)

i = {x for x in [1] if x > 0 for y in [2]}

type(i)

j = {x: x for x in [1] if x > 0 for y in [2]}

type(j)

k = {x for x in [1] if x > 0 for y in [2] if y > 1}

type(k)

l =
