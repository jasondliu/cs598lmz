import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint8),
                ("b", ctypes.c_uint8)]
    TYPE_FILTER = True

ctypes.c_int8(-13).value # ok
ctypes.c_uint8(252).value # ok
X().a = 3 # ok
X().a = 256 # error

# Test ctypes.Structure
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint8),
                ("b", ctypes.c_uint8)]
X().a = 3 # ok
X().a = 256 # error
