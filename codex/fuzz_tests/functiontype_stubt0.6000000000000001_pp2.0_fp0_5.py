from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])

def f1():
    yield 1

def f2():
    yield 2

def f3():
    yield 3

d = f1()
e = f2()
f = f3()

f1() is f1()

f1() is d

f

a.__iter__() is a

b.__iter__() is b

c.__iter__() is c

d.__iter__() is d

e.__iter__() is e

f.__iter__() is f

def g1():
    return 1

def g2():
    return 2

def g3():
    return 3

g = g1()
h = g2()
i = g3()

g1() is g1()

g1() is g

h

def gen():
    for i in range(3):
        yield i

g = gen()
g

next(g)

next(g
