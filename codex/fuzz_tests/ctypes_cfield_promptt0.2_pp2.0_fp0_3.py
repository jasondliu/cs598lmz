import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField),
                ("c", ctypes.c_int)]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int)]

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
