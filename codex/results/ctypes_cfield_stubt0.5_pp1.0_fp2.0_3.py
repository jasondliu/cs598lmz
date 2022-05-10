import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(object):
    def __getitem__(self, key):
        return key

def f1(x):
    return x[0]

def f2(x):
    return x[0]

def f3(x):
    return x[0]

def f4(x):
    return x[0]

def f5(x):
    return x[0]

def f6(x):
    return x[0]

def f7(x):
    return x[0]

def f8(x):
    return x[0]

def f9(x):
    return x[0]

def f10(x):
    return x[0]

def f11(x):
    return x[0]

def f12(x):
    return x[0]

def f13(x):
    return x[0]

def f14(x):
    return x[0]

def f15(x):
    return x[0]

def f16(x
