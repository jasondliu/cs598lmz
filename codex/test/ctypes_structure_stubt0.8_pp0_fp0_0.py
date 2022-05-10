import ctypes

class S(ctypes.Structure):
    x = 1

print (S().x)
# 1
