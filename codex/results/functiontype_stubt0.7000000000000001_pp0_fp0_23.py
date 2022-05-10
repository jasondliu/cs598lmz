from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
c = (x for x in [1])
d = (x for x in [1])

a.__class__

print(a.__class__)

print(b.__class__)

print(c.__class__)

print(d.__class__)

print(a is b)

print(a is c)

print(a is d)

print(x for x in [1] is (x for x in [1]))

f = lambda x: x

print(f.__class__)

print(type(f))

print(f is lambda x: x)

print(f is lambda x: x)

def f(x):
    return x

def g(x):
    return x

print(f is g)

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

print(f is g)

print(f is h)

print
