import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.POINTER(ctypes.c_uint)

s = S()
a = ctypes.c_uint()
a.value = 5
s.y = ctypes.pointer(a)

