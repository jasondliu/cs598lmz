import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
s = POINT.in_dll(ctypes.CDLL("libc.so.6"), "errno")
print(s.x, s.y)
# Test ctypes.CDLL with RTLD_GLOBAL, and ctypes.CField
# The order is important, because gcc is picky about putting
# extern data into DSOs...
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]
libc = ctypes.CDLL("libc.so.6", mode=ctypes.RTLD_GLOBAL)
s = POINT.in_dll(libc, "errno")
print(s.x, s.y)
s.x = 12
print(s.x, s.y)
# Test ctypes.CDLL with RTLD_GLOBAL, and ctypes.Py_
