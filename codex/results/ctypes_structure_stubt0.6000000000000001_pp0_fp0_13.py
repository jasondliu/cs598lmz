import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int
    _fields_ = [ ("x", ctypes.c_int), ("y", ctypes.c_int), ("z", ctypes.c_int) ]

a = S()

print a.x
print a.y
print a.z
print a

a.x = 35
a.y = 36
a.z = 37

print a.x
print a.y
print a.z
print a
