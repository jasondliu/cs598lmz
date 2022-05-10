import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print ctypes.addressof(s)
print ctypes.addressof(s.x)
print ctypes.addressof(s.y)

print ctypes.sizeof(s)
print ctypes.sizeof(s.x)
print ctypes.sizeof(s.y)
