import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_double, ctypes.c_int, ctypes.POINTER( ctypes.c_double ),  ctypes.POINTER( ctypes.c_double ), ctypes.POINTER(ctypes.c_void_p) )

class GenInterface(object):
    def __init__(self):
        self.fg=ctypes.CDLL('./gen.so')
        self.fg.gen.restype = ctypes.c_double
        self.fg.gen.argtypes = [ ctypes.c_int, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_void_p) ]
        self.fg.create.restype = ctypes.c_void_p
        self.fg.create.argtypes = [ ctypes.c_int ]
        self.fg.destroy.restype = ctypes.c_void_p
        self.fg.destroy.argtypes = [ ctypes.c_void_p ]
        self.fg.set
