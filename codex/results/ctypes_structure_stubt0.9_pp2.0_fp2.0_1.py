import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong

    # XXX TODO: the alignment of a pointer must be its size
    #_anonymous_ = ("x",)
    _fields_ = [("y", ctypes.POINTER(x))]

assert ctypes.calcsize("P") == ctypes.sizeof(ctypes.c_void_p)
