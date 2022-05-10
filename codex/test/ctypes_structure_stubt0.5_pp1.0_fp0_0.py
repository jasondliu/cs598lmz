import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char * 4

def foo(s):
    s.x = 'spam'
    return s

s = S()
s.x = 'eggs'
