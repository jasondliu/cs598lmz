import ctypes
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
a = A.from_address(10)
a.a
