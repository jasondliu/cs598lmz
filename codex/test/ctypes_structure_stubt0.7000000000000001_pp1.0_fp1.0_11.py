import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

p = ctypes.pointer(S())
p.contents.x = 42
p.contents.y = 24
