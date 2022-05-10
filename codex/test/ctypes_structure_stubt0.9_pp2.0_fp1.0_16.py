import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

a = S()
a.x = 1
a.y = 2

s = ctypes.string_at(ctypes.addressof(a), ctypes.sizeof(a))
new_a = ctypes.cast(ctypes.c_char_p(s), ctypes.POINTER(S)).contents
