import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class T(ctypes.Structure):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class U(ctypes.Union):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

class V(ctypes.Union):
    x = 1
    _fields_ = [('y', ctypes.c_int)]

