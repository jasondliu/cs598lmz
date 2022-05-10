import ctypes
# Test ctypes.CField instance
import ctypes
try:
    ctypes.CField("_", "", "", "", "")
except TypeError:
    print("SKIP")
    raise SystemExit

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

s = S(4, 5)
print(s.a)
print(s.b)
