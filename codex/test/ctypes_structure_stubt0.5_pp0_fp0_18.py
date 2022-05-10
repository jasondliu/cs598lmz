import ctypes

class S(ctypes.Structure):
    x = ctypes.c_char_p
    y = ctypes.c_char_p
    z = ctypes.c_char_p

s = S()
s.x = 'x'
s.y = 'y'
s.z = 'z'

assert s.x == 'x'
assert s.y == 'y'
assert s.z == 'z'
