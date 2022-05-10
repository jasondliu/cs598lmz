import ctypes
# Test ctypes.CField.
INT64 = ctypes.c_int64
UINT64 = ctypes.c_uint64

class N(ctypes.Structure):

    _fields_ = [("one", ctypes.CField, 4),
                ("two", ctypes.CField, 4),
                ("three", ctypes.CField, 4),
                ("four", ctypes.CField, 4),
                ("five", ctypes.CField, 4),
                ("six", ctypes.CField, 4),
                ("seven", ctypes.CField, 4),
                ("eight", ctypes.CField, 4),
                ("nine", ctypes.CField, 4),
                ("ten", ctypes.CField, 4),
                ("eleven", ctypes.CField, 4) ]

class F(ctypes.Structure):
    _fields_ = [("a", N),
                ("b", N)]

class G(ctypes.Union):
    _fields_ = [("a", N),
                ("b", N)]

class H(ctypes.Structure):

