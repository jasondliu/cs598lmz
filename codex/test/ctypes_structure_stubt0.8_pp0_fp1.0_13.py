import ctypes

class S(ctypes.Structure):
    x = ctypes.POINTER(ctypes.c_int)
s = S()
s.x = ctypes.pointer(ctypes.c_int())

def f(p):
    p = ctypes.cast(ctypes.pointer(ctypes.c_int()), ctypes.c_void_p)
