import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
assert fun.__name__ == 'fun'

# SF bug #1673295:
try:
    ctypes.cdll.LoadLibrary("libc.so").gets
except AttributeError:
    pass
else:
    raise Exception("AttributeError not raised")

# SF bug #1741791:
libm = ctypes.cdll.LoadLibrary(ctypes.util.find_library("m"))
libm.sin.argtypes = [ctypes.c_double]
libm.sin.restype = ctypes.c_double

# SF bug #1721090:
try:
    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
except TypeError:
    pass
else:
    raise Exception("TypeError not raised")

# SF bug #1736142:
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.
