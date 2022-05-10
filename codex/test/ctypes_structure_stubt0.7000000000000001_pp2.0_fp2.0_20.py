import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte()
    y = ctypes.c_ubyte()
    z = ctypes.c_ubyte()

def f(s):
    print(s.x, s.y, s.z)

