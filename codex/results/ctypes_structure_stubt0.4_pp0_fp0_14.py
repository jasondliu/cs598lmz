import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S(1, 2)
print(s.x, s.y)

print(ctypes.sizeof(s))

print(ctypes.addressof(s))
print(ctypes.addressof(s.x))
print(ctypes.addressof(s.y))

print(ctypes.get_errno())

ctypes.set_errno(2)
print(ctypes.get_errno())
