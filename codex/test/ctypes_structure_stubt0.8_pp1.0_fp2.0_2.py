import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong(10)

def func(arg):
    return arg.x

lib = ctypes.CDLL(None)
