import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class T(ctypes.Structure):
    a = ctypes.c_double
    b = ctypes.c_double
    c = ctypes.c_double

class U(ctypes.Structure):
    l = ctypes.c_double
    m = ctypes.c_double
    n = ctypes.c_double

class V(ctypes.Structure):
    d = ctypes.c_double
    e = ctypes.c_double
    f = ctypes.c_double

class W(ctypes.Structure):
    g = ctypes.c_double
    h = ctypes.c_double
    i = ctypes.c_double

class X(ctypes.Structure):
    j = ctypes.c_double
    k = ctypes.c_double
    _fields_ = [
        ('j', ctypes.c_double),
        ('k', ctypes.c_double),
        ('
