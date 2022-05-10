import types
# Test types.FunctionType

def f():
    pass

def g(x):
    return x

def h(x, y):
    return (x, y)

def i(x, y, z):
    return (x, y, z)

def j(x, y, z=1):
    return (x, y, z)

def k(x, y=1, z=2):
    return (x, y, z)

def l(x, *args):
    return (x,) + args

def m(x, **kwargs):
    return (x,) + tuple(kwargs.items())

def n(x, *args, **kwargs):
    return (x,) + args + tuple(kwargs.items())

def o(x, *, y, z):
    return (x, y, z)

def p(x, *, y=1, z=2):
    return (x, y, z)

def q(x, y=1, *, z):
    return (x, y, z)


