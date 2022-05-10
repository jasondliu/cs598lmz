import ctypes
# Test ctypes.CFields.

import ctypes

class CFoo(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

f = CFoo()
f.x = 1
f.y = 2
print(f.x, f.y)
f.x = -100
f.y = 9
print(f.x, f.y)
