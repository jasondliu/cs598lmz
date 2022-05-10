import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ctypes.CField("e", ctypes.c_int),
                ctypes.CField("f", ctypes.c_int),
                ctypes.CField("g", ctypes.c_int),
                ctypes.CField("h", ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ctypes.CField("e", ctypes.c_int),
                ctypes.CField("f", ctypes.c_int),
                ctypes.CField("g", ctypes.c_int),
                ctypes.CField("h
