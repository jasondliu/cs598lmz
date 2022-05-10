import ctypes
# Test ctypes.CField.create with different types

class A(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class B(ctypes.Structure):
    _fields_ = [("a", A),
                ("b", ctypes.c_char * 10)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 10),
                ("b", ctypes.c_char * 10)]

class D(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 10),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_char * 10)]

class E(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char * 10),
                ("b", ctypes.c_char * 10),
                ("c", ctypes
