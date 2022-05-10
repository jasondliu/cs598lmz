import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ("a",)

# Test ctypes.Field
class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ("a",)

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]
    _anonymous_ = ("a",)

# Test ctypes.Union
class G(ctypes.Union):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

class H(ctypes.Union):
    _fields_ = [("a", c
