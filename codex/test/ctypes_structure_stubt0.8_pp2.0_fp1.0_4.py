import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char

s = S()
s.x = 'a'
assert s.x == 'a'
assert s.x != 'b'

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_char)]

s = S()
