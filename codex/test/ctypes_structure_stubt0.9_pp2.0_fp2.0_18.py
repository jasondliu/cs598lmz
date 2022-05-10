import ctypes

class S(ctypes.Structure):
    x = 10

s = S()
print(ctypes.addressof(s))
