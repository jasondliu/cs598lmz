fn = lambda: None
# Test fn.__code__

def f():
    pass

def g():
    1 + 2

def h(x):
    return x

def i(x, y):
    return x, y

def j(x, y, z):
    return x, y, z

def k(x, y=1, z=2):
    return x, y, z

def l(x, *y):
    return x, y

def m(x, **y):
    return x, y

def n(x, *y, **z):
    return x, y, z

def o(x, y=1, *z, **t):
    return x, y, z, t

def p(x, y, z=1, *t, **u):
    return x, y, z, t, u

def q(x, y, z=1, *t, a, **u):
    return x, y, z, t, a, u

def r(x, y, z=1, *t, a=3, **u):
