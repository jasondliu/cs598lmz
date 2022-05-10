import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_float()

p = ctypes.pointer(S())
p.contents.x
p.contents.y
