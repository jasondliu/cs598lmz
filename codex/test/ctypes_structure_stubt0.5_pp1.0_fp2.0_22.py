import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ulong
    y = ctypes.c_ulong
    z = ctypes.c_ulong

class M(ctypes.Structure):
    x = ctypes.c_ulong
    y = ctypes.c_ulong
    z = ctypes.c_ulong

class V(ctypes.Structure):
    x = ctypes.c_ulong
    y = ctypes.c_ulong
    z = ctypes.c_ulong

class Point(ctypes.Structure):
    x = ctypes.c_ulong
    y = ctypes.c_ulong
    z = ctypes.c_ulong

class Triangle(ctypes.Structure):
    v1 = V()
    v2 = V()
    v3 = V()

class Material(ctypes.Structure):
    r = ctypes.c_float
    g = ctypes.c_float
    b = ctypes.c_float
    spec = ctypes.c_float
    refl = ctypes.c_float
