import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "b", ctypes.c_int))]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", ctypes.c_int))]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", ctypes.c_int, 1))]

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField(C, "a", ctypes.c_int, 2))]

class H
