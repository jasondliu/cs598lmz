import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double

class T(ctypes.Structure):
    a = ctypes.c_longlong
    b = ctypes.c_double
    c = S
    d = ctypes.c_longlong

class U(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double
    z = ctypes.c_longlong
    t = T
    u = T
    v = ctypes.c_longlong

class V(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double
    z = ctypes.c_longlong
    t = T
    u = T
    v = ctypes.c_longlong

class W(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_double
    z = ctypes.c_longlong
    t = T
    u = T
