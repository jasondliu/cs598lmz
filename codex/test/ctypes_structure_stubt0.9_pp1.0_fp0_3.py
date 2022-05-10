import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_float

print("%d" % ctypes.sizeof(S))
