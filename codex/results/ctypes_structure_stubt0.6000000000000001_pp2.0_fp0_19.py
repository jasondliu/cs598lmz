import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

    def __str__(self):
        return 'x=%d, y=%d' % (self.x, self.y)

class T(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

    def __str__(self):
        return 'x=%d, y=%d' % (self.x, self.y)

lib = ctypes.CDLL('./libtest.so')

lib.S_init.argtypes = [ctypes.POINTER(S)]
lib.S_init.restype = None

lib.T_init.argtypes = [ctypes.POINTER(T)]
lib.T_init.restype = None

#lib.get_S.restype = ctypes.POINTER(S)
#lib.get_T.restype = ctypes.POINTER(T)

lib.get_S.restype = ctypes.c_void_p

