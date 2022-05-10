import ctypes
# Test ctypes.CField

# All of the following should work

class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_char_p)]

class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char_p),
                ("c", ctypes.c_int)]

class CField(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int * 3)]

class CField(ctypes.St
