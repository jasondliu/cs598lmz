import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __init__(self):
        self.x = ctypes.c_int()

class Y(object):
    def __init__(self):
        self.x = ctypes.c_int()

class Z(object):
    def __init__(self):
        self.x = ctypes.c_int()
        self.z = ctypes.c_void_p()

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

def f():
    return ctypes.c_int()

def g():
    return ctypes.c_int()

def h():
    return ctypes.c_int()

def i():
    return ctypes.c_int()

def j():
    return ctypes.c_int()

def k():
    return ctypes.c_int()

def l():
    return ctypes.c_int()

def m():
    return ctypes.c_int()

def n():
