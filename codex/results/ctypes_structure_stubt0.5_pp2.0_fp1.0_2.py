import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
s.x = 1
s.y = 2
s.z = 3

ctypes.memmove(ctypes.byref(s), ctypes.byref(s.y), ctypes.sizeof(s.y))

print s.x
print s.y
print s.z
</code>

