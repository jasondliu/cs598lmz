import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()

s = S()
print s.x

a = ctypes.c_double(1.0)
print a.value

print ty
