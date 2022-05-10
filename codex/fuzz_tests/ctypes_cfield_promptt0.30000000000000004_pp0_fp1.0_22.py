import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a"]

class CTest2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a", "b"]

class CTest3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["a", "b", "c"]

class CTest4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
    _anonymous_ = ["c"]

class CTest5(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int
