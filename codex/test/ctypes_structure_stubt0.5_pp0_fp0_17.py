import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4

s = S()

s.x = b'abc'

print(s.x)
