import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte * 3

class T(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte)]

class U(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("c", ctypes.c_byte)]

class V(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("c", ctypes.c_byte),
                ("d", ctypes.c_byte)]

class W(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte),
                ("b", ctypes.c_byte),
                ("c", ctypes.c_byte),
                ("d", ctypes.c_byte),
                ("e", ctypes.c_byte)]

class X(ctypes.Structure):
    _fields
