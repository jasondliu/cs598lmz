import ctypes

class S(ctypes.Structure):
    x = ctypes.c_byte * 5

s = S()
p = ctypes.cast(ctypes.byref(s), ctypes.POINTER(None))
