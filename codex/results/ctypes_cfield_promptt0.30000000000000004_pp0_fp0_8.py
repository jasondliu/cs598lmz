import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.c_char_p)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField("a", ctypes.c_char_p, 1))]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField("a", ctypes.c_char_p, 2))]

class F(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField("a", ctypes.c_char_p, 3))]

class G(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p),
                ("b", ctypes.CField("a", ctypes.c
