import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

print s.x, s.y, s.z

print ctypes.sizeof(S)
print ctypes.sizeof(ctypes.c_int)

print ctypes.addressof(s)
print ctypes.addressof(s.x)
print ctypes.addressof(s.y)
print ctypes.addressof(s.z)

print ctypes.addressof(s) == ctypes.addressof(s.x)
print ctypes.addressof(s.x) == ctypes.addressof(s.y) - ctypes.sizeof(ctypes.c_int)
print ctypes.addressof(s.y) == ctypes.addressof(s.z) - ctypes.sizeof(ctypes.c_int)

print ctypes.addressof(s.
