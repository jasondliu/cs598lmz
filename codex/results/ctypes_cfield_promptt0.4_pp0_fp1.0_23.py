import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char)]

class D(ctypes.Structure):
    _fields_ = [("s", S),
                ("c", ctypes.c_char),
                ("d", ctypes.c_char)]

class E(ctypes.Structure):
    _fields_ = [("c", ctypes.c_char),
                ("s", S),
                ("d", ctypes.c_char)]

class F(ctypes.Structure):
    _fields_ = [("c", ctypes.c_char),
                ("d", ctypes.c_char),
                ("s", S)]

class G(ctypes.Structure):
    _fields_ = [("c", ctypes.c_char),
                ("s", S),
                ("d",
