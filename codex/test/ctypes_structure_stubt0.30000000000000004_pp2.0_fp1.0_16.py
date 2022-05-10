import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p

s = S()
s.x = 'abc'
s.y = 'def'

