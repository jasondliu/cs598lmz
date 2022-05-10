import types
# Test types.FunctionType

def a():
    pass

def b(x):
    return x

def c(x, y):
    return x, y

def d(x, y, z=1):
    return x, y, z

def e(x, y, z=1, *t):
    return x, y, z, t

def f(x, y, z=1, *t, **d):
    return x, y, z, t, d

def g(x, y, z=1, *t, u, v=2, **d):
    return x, y, z, t, u, v, d

def h(x, y, *, u=1, v=2):
    return x, y, u, v

def i(x, y, *args, u=1, v=2, **kw):
    return x, y, args, u, v, kw

def j(x, y, z=1, *, u=1, v=2):
    return x, y, z, u, v
