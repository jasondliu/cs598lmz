import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

class T(ctypes.Structure):
    a = ctypes.c_int
    b = S

class U(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2

class V(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2 * 3

class W(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2 * 3 * 4

class X(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2 * 3 * 4 * 5

class Y(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2 * 3 * 4 * 5 * 6

class Z(ctypes.Structure):
    a = ctypes.c_int
    b = S * 2 * 3 * 4 * 5 * 6 * 7

class ZZ(ctypes.Structure):
    a
