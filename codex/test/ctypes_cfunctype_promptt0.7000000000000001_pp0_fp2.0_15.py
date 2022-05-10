import ctypes
# Test ctypes.CFUNCTYPE
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 1

