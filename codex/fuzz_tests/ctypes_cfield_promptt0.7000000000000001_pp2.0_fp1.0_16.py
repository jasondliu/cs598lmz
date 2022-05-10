import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("f", ctypes.CField)]

class D(ctypes.Structure):
    _anonymous_ = ("f",)
    _fields_ = [("f", ctypes.CField), ("a", ctypes.c_int)]

class E(ctypes.Structure):
    _fields_ = [("f", ctypes.CField)]

# Test ctypes.Field
class F(ctypes.Structure):
    _fields_ = [("f", ctypes.Field)]

class G(ctypes.Structure):
    _anonymous_ = ("f",)
    _fields_ = [("f", ctypes.Field), ("a", ctypes.c_int)]

class H(ctypes.Structure):
    _fields_ = [("f", ctypes.Field)]

# Test ctypes.Array
class I(ctypes.Structure):
    _fields_ = [("f", ctypes.Array)]

class J(ctypes.Structure):
    _anonymous
