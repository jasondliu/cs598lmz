import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte
    y = ctypes.c_byte
    z = ctypes.c_short
    _pack_ = 1

def f():
    return S(x=1, y=2, z=3)

