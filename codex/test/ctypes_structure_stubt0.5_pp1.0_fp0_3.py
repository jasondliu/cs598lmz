import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 10

s = S()
s.x = "hello"

