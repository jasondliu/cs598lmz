import ctypes

class S(ctypes.Structure):
    x = []

s = S()
print(repr(s))
