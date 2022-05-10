import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

# Look ma, no compilation!
print S.x
