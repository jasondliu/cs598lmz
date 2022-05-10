import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_void_p
    z = ctypes.c_void_p

s = S()
print repr(s)

s.x = 1
s.y = 10
s.z = 10
print repr(s)

s.x = 2
s.y = 20
s.z = 20
print repr(s)
