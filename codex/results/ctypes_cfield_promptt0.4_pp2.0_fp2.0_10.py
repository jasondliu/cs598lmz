import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("b", ctypes.c_int),
                ("a", ctypes.CField)]

class Z(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.c_int)]

class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField)]

class B(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField),
                ("c", ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.CField),
                ("b", ctypes.c_int),
                ("c", ctypes.c
