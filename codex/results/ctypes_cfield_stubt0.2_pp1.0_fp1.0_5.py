import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self, x):
        self.x = x

class D(C):
    def __init__(self, x):
        C.__init__(self, x)

def f(x):
    return x

def g(x):
    return x

def h(x):
    return x

def i(x):
    return x

def j(x):
    return x

def k(x):
    return x

def l(x):
    return x

def m(x):
    return x

def n(x):
    return x

def o(x):
    return x

def p(x):
    return x

def q(x):
    return x

def r(x):
    return x

def s(x):
    return x

def t(x):
    return x

def u(x):
    return x

def v(x):
    return x

def w(x):
    return x


