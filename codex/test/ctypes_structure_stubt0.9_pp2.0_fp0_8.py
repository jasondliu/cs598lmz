import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

i = S()
s = ctypes.string_at(ctypes.byref(i), ctypes.sizeof(i))
new = ctypes.cast(ctypes.c_char_p(s), ctypes.POINTER(S))
print(new.contents.x, new.contents.y)
