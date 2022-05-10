import ctypes
# Test ctypes.CField
class T(ctypes.Structure):
    _fields_ = [("x", ctypes.c_void_p),
                ("y", ctypes.POINTER(ctypes.c_int)),
                ("z", ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p))]
lib.TpConstruct.argtypes = [ctypes.POINTER(T)]

class Tp(ctypes.c_void_p):
    def __init__(self):
        t = T()
        lib.TpConstruct(ctypes.byref(t))
        self.value = t.x.value
        self.y = t.y
        self.z = t.z
#
# Test ctypes.c_char_p
#

lib.echo.restype = ctypes.c_char_p
lib.echo.argtypes = [ctypes.c_char_p, ctypes.c_int]

s = "Hello World"
b = bytes(s, "latin1")

# null terminated string:
