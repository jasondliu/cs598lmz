import ctypes
# Test ctypes.CField

class S1(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class S2(ctypes.Structure):
    _anonymous_ = ["b"]

    _fields_ = [("a", ctypes.c_int),
                ("b", S1)]

class S3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                (None, ctypes.c_int),
                ("b", ctypes.c_int),
                (None, ctypes.c_int),
                ("c", ctypes.c_int),
                (None, ctypes.c_int),
                ("d", ctypes.c_int),
                (None, ctypes.c_int),
                ("e", ctypes.c_int),
                (None, ctypes.c_int),
                ("f", ctypes.c_int),
                (None, ctypes.c_int),
                ("g", ctypes.c_int),
                (None, ctypes
