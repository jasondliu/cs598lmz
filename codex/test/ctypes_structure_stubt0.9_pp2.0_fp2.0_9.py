import ctypes

class S(ctypes.Structure):
    x = 1

s = S()
print(s.x)
