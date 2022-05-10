import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()

def f(x):
    return x*x

def g(x):
    return x*x*x

def h(x):
    return x*x*x*x

def i(x):
    return x*x*x*x*x

def j(x):
    return x*x*x*x*x*x

def k(x):
    return x*x*x*x*x*x*x

def l(x):
    return x*x*x*x*x*x*x*x

def m(x):
    return x*x*x*x*x*x*x*x*x

def n(x):
    return x*x*x*x*x*x*x*x*x*x

def o(x):
    return x*x*x*x*x*x*x*x*x*x*x

def p(x):
    return x*x*x*x
