import ctypes

class S(ctypes.Structure):
    x = bytearray(100)

s = S()
