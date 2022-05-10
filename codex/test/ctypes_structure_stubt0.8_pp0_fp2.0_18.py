import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(2.0)

s = S()
print("Original:", s.x)
double_ptr = ctypes.cast(ctypes.byref(s), ctypes.POINTER(ctypes.c_double))
double_ptr[0] = 3.0
print("Changed:", s.x)
