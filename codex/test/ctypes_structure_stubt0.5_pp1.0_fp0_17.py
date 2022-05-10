import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte
    y = ctypes.c_ubyte

a = ctypes.c_ubyte(1)
b = ctypes.c_ubyte(2)
c = ctypes.c_ubyte(3)
d = ctypes.c_ubyte(4)

