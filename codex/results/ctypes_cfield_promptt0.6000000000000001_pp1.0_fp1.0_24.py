import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.CField)
    ]

s = S()
ctypes.memset(ctypes.addressof(s), 0, ctypes.sizeof(s))

s.a = 1
s.b = 2

print(s.a, s.b)
