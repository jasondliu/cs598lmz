import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte

i = S()
s = '\xc1\x9f'
ctypes.memmove(ctypes.addressof(i), s, len(s))

