import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class D(ctypes.Union):
    _fields_ = [("b", ctypes.c_int),
                ("c", ctypes.c_int)]

# - Test ctypes.CField on Structures
try:
    C.x = ctypes.CField("x")
except AttributeError:
    pass
else:
    raise RuntimeError("Expected AttributeError")

try:
    C.y = ctypes.CField("y", ctypes.c_int)
except AttributeError:
    pass
else:
    raise RuntimeError("Expected AttributeError")

try:
    C.z = ctypes.CField("z", ctypes.c_int, 0)
except AttributeError:
    pass
else:
    raise RuntimeError("Expected AttributeError")

C.x = ctypes.CField("x", ctypes.c_int, 1)
C.y = ctypes.CField("y
