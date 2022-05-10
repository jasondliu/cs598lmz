import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

ss = ctypes.cast(ctypes.pointer(S()), ctypes.c_void_p)
