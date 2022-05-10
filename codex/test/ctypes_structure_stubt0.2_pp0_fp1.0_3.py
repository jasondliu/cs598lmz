import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

def f(x, y):
    return x + y

def g(x, y):
    return x - y

def h(x, y):
    return x * y

def i(x, y):
    return x / y

def j(x, y):
    return x % y

def k(x, y):
    return x & y

def l(x, y):
    return x | y

def m(x, y):
    return x ^ y

def n(x, y):
    return x << y

def o(x, y):
    return x >> y

def p(x, y):
    return x ** y

def q(x, y):
    return x // y

def r(x, y):
    return x == y

def s(x, y):
    return x != y

def t(x, y):
    return x < y

