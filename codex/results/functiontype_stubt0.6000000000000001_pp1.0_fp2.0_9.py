from types import FunctionType
a = (x for x in [1])
b = [1]
a

b

c = list(a)
c

c = [x for x in [1]]
c

def f(x):
    return [x for x in [1]]

f

type(f)

type(f) == FunctionType

def g():
    return [1]

g

type(g)

type(g) == FunctionType

type(g())

type(f)

type(f())

type(f) == FunctionType

type(f) == type(g)

type(f()) == type(g())

type(f()) == list

type(g()) == list

type([1])

a = [1]

type(a)

type(a) == list

type(a) == type([1])

type(a) == type([x for x in [1]])

type(a) == type(f())

type(a) == type(g())

b = []

type(b)


