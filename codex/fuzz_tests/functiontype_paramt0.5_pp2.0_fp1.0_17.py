from types import FunctionType
list(FunctionType(lambda:0,globals()))[0]

#2.
def f(x):
    return lambda y:x+y

t=f(1)
t(2)

#3.
def f(x):
    return lambda y:x+y

t=f(1)
t(3)

#4.
def f(x):
    return lambda y:x+y

t=f(1)
t(4)

#5.
def f(x):
    return lambda y:x+y

t=f(1)
t(5)

#6.
def f(x):
    return lambda y:x+y

t=f(1)
t(6)

#7.
def f(x):
    return lambda y:x+y

t=f(1)
t(7)

#8.
def f(x):
    return lambda y:x+y

t=f(1)
t(8)

#9.
def f(x):

