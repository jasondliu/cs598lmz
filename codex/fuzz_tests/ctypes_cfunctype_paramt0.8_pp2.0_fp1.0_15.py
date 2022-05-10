import ctypes
FUNTYPE = ctypes.CFUNCTYPE(
    ctypes.c_void_p, #return type
    ctypes.c_int, #arg 1 type
    ctypes.c_int, #arg 2 type
    ctypes.c_int, #...
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int, #arg 8 type
)

class pypushmap(object):
    def __init__(self):
        self.lib = ctypes.CDLL("libparser.so")
        self.lib.pushmap.argtypes = [ctypes.c_int, ctypes.c_int,ctypes.c_int,ctypes.c_int, FUNTYPE]
        self.lib.pushmap.restype = ctypes.c_void_p
        self.lib.freemap.argtypes = [ctypes.c_void_p]
        self.lib.freemap.restype = None
        self.lib.writemap.argtypes = [ctypes
