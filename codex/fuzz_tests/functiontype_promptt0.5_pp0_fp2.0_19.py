import types
# Test types.FunctionType

def f(a, b):
    return a + b

def g():
    return 1

def h(a):
    return a

def i(a, b, c):
    return a + b + c

def j(a, b, c, d):
    return a + b + c + d

def k(a, b, c, d, *args):
    return a + b + c + d + sum(args)

def l(a, b, c, d, *args, **kwargs):
    return a + b + c + d + sum(args) + sum(kwargs.values())

def m(a, b, c, d, *args, **kwargs):
    return a + b + c + d + sum(args) + sum(kwargs.values())

def n(a, b, c, d, *args, **kwargs):
    return a + b + c + d + sum(args) + sum(kwargs.values())

def o(a, b, c, d, *args, **kw
