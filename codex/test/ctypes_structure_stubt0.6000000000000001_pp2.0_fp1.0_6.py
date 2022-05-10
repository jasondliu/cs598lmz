import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64()
    y = ctypes.c_uint64()
    z = ctypes.c_uint64()

def f(s):
    s.x = s.y + s.z

a = S()
a.x = 1
a.y = 2
a.z = 3
f(a)
print(a.x)
