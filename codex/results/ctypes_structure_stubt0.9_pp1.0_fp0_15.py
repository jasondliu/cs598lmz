import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte * 5

s = S()
p = ctypes.cast(ctypes.byref(s), ctypes.POINTER(None))
print ctypes.cast(ctypes.byref(ctypes.cast(p, ctypes.c_void_p), \
        ctypes.POINTER(ctypes.c_longlong)), ctypes.POINTER(None))
