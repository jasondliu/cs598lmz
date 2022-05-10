import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class CBar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("foo", CFoo)]

class CBar2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("foo", CFoo),
                ("bar", CBar)]

class CBar3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("foo", CFoo),
                ("bar", CBar),
                ("bar2", CBar2)]

class CBar4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int
