import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    pass
S2._fields_ = [('x', ctypes.c_int)]

class S3(ctypes.Structure):
    _pack_ = 4
    _fields_ = [('x', ctypes.c_int)]

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char)]

try:
    # The ctypes module is only available in a debug build
    ctypes.c_ssize_t
except AttributeError:
    pass
else:
    class S5(ctypes.Structure):
        _fields_ = [('x', ctypes.c_ssize_t)]

try:
    # The ctypes module is only available in a debug build
    ctypes.c_ssize_t
except AttributeError:
    pass
else:
    class S6(ctypes.Structure):
        _fields_ = [('x', ctypes.c_ssize_t), ('y', ctypes.c_char)]

