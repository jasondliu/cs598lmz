import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double

e = ctypes.POINTER(S)()

e = ctypes.pointer(S())
e.contents.x = 1.0
e.contents.y = 2.0

