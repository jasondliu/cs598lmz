import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_float(2.0)

s = S()

print(s.x)
print(s.y)

S.x = ctypes.c_int(2)
S.y = ctypes.c_float(2.5)

print(s.x)
print(s.y)
