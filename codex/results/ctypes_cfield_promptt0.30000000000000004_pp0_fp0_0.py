import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b",)

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b", "a")

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b", "a", "b")

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ("b", "a", "b", "a")

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c
