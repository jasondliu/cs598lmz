import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_bool * 200)()

s = S()
