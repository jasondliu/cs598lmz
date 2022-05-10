import ctypes
ctypes.cast(b'string', ctypes.POINTER(ctypes.c_ubyte))
class cls_example(ctypes.Structure):
    _fields_ = [('a', ctypes.c_ubyte), ('b', ctypes.c_ubyte)]
ctypes.cast(b'AB', ctypes.POINTER(cls_example))

# example 2
libm = ctypes.CDLL(ctypes.util.find_library('m'))
libm.cos.argtypes = [ctypes.c_double]
libm.cos.restype = ctypes.c_double

# see Argument Type Objects
class coordinate(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

# how to pass this class to C?
# see Python C Object Interface (PyCOI)
# - "C to Python (C2P) Type Convensions"
# - "Python to C (P2C) Type Convensions"

# see Sequence Protocol
