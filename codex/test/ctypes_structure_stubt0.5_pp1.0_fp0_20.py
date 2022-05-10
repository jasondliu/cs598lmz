import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double
    w = ctypes.c_double

class V(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class M(ctypes.Structure):
    m11 = ctypes.c_double
    m12 = ctypes.c_double
    m13 = ctypes.c_double
    m14 = ctypes.c_double
    m21 = ctypes.c_double
    m22 = ctypes.c_double
    m23 = ctypes.c_double
    m24 = ctypes.c_double
    m31 = ctypes.c_double
    m32 = ctypes.c_double
    m33 = ctypes.c_double
    m34 = ctypes.c_double
    m41 = ctypes.c_double
    m42 = ctypes.c_double
    m43 = ctypes.c_double
   
