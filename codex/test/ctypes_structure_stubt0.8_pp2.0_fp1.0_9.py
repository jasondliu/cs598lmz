import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32()
    s = ctypes.c_char_p(b'foo')

x = S()
print(x)
