import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("first", ctypes.c_uint32),
                ("second", ctypes.c_uint32)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint32),
                ("b", ctypes.c_uint32),
                ("c", ctypes.c_uint32),
                ("d", ctypes.c_uint32),
                ("e", ctypes.c_uint32),
                ("f", ctypes.c_uint32),
                ("g", ctypes.c_uint32),
                ("h", ctypes.c_uint32),
                ("i", ctypes.c_uint32),
                ("j", ctypes.c_uint32),
                ("k", ctypes.c_uint32),
                ("l", ctypes.c_uint32),
                ("m", ctypes.c_uint32),
                ("n", ctypes.c_uint32),
                ("o", ctypes.c_uint32),
                ("
