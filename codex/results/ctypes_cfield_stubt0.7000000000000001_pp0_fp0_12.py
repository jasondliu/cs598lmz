import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class S4(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

class S5(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

class S6(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)]

class S7(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_int)]

class S8(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('y', ctypes.c_void_p)]

class S9(ctypes.St
