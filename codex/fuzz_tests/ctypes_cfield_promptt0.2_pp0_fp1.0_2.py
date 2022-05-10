import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class CBar(ctypes.Structure):
    _fields_ = [("foo", CFoo),
                ("c", ctypes.c_int)]

class CBaz(ctypes.Structure):
    _fields_ = [("bar", CBar),
                ("d", ctypes.c_int)]

class CQux(ctypes.Structure):
    _fields_ = [("baz", CBaz),
                ("e", ctypes.c_int)]

class CQux2(ctypes.Structure):
    _fields_ = [("baz", CBaz),
                ("e", ctypes.c_int)]

class CQux3(ctypes.Structure):
    _fields_ = [("baz", CBaz),
                ("e", ctypes.c_int)]

class CQux4(ctypes.Structure):
    _fields_ = [("b
