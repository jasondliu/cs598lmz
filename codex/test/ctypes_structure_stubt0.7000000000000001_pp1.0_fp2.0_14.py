import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

def foo():
    return ctypes.sizeof(S)

print(foo())
