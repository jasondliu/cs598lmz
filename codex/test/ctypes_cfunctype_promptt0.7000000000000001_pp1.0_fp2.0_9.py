import ctypes
# Test ctypes.CFUNCTYPE
#
# This test passes if it runs without crashing.

def get_method(lib, name):
    method = getattr(lib, name)
    method.restype = ctypes.c_int
    method.argtypes = ()
    return method

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.POINTER(X)),
                ]

