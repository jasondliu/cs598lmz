import ctypes
# Test ctypes.CFUNCTYPE.
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

def callback(x):
    x.a = 7

