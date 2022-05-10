import ctypes

class S(ctypes.Structure):
    x = ctypes.c_long()

foo = S()
foo.x = -2
