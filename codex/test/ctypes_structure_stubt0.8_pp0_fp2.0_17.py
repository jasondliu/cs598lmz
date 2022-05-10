import ctypes

class S(ctypes.Structure):
    x = slice(1, 2, 3)
S()
