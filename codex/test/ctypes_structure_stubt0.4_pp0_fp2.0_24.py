import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

def f():
    return S(1, 2)

