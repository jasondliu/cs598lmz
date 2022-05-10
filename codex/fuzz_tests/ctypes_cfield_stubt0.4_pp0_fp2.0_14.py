import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self):
        self.x = 42

class Y(X):
    pass

def f():
    pass

def f(x):
    pass

def f(x):
    pass

def f(x, y):
    pass

def f(x, y, z):
    pass

def f(x, y, z, w):
    pass

def f(x, y, z, w, t):
    pass

def f(x, y, z, w, t, u):
    pass

def f(x, y, z, w, t, u, v):
    pass

def f(x, y, z, w, t, u, v, r):
    pass

def f(x, y, z, w, t, u, v, r, s):
    pass

def f(x, y, z, w, t, u, v, r, s, q):
    pass

def f(x, y, z, w, t
