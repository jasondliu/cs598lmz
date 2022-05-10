import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def c_func(x):
    return x**2

c_fun = FUNTYPE(c_func)

class C_FUN(object):
    def __init__(self, c_fun):
        self.c_fun = c_fun
    def __call__(self, x):
        return self.c_fun(x)

c_fun = C_FUN(c_fun)

def f(x):
    return x**2

def g(x):
    return x**3

def h(x):
    return x**4

def k(x):
    return x**5

def l(x):
    return x**6

def m(x):
    return x**7

def n(x):
    return x**8

def o(x):
    return x**9

def p(x):
    return x**10

def q(x):
    return x**11

def r(x):
    return x**12

