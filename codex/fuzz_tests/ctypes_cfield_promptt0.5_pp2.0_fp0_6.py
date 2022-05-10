import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int),
                ("k", ctypes.c_int),
                ("l", ctypes.c_int),
                ("m",
