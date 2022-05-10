import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

@FUNTYPE
def f(x):
    return sin(x)

@FUNTYPE
def g(x):
    return x

@FUNTYPE
def h(x):
    return x**2

@FUNTYPE
def i(x):
    return x**3

@FUNTYPE
def j(x):
    return x**4

@FUNTYPE
def k(x):
    return x**5

@FUNTYPE
def l(x):
    return x**6

@FUNTYPE
def m(x):
    return x**7

@FUNTYPE
def n(x):
    return x**8

@FUNTYPE
def o(x):
    return x**9

@FUNTYPE
def p(x):
    return x**10

@FUNTYPE
def q(x):
    return x**11

@FUNTYPE
def r(x):
    return x**12

@FUNTYPE
def s(x):
    return x**13

@FUN
