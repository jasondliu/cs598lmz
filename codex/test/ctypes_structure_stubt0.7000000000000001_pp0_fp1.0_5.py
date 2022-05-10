import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

x = S()
#x.x = 1
