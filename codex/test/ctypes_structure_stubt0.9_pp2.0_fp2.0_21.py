import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    #ctypes.POINTER(ctypes.c_void_p)
