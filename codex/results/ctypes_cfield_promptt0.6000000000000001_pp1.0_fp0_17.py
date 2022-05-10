import ctypes
# Test ctypes.CField
import ctypes

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double)]

class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.CField(S))]

s = S2()
s.a = S()
s.a.a = 1.0

print(s.a.a)
