from types import FunctionType
a = (x for x in [1])
type(a)

for x in a:
    print(x)

type(a)

b = a
type(b)

type(a)
