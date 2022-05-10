import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()
    foo = ctypes.c_char_p()

s = S()
s.x = 1.0
s.y = 0.0
s.z = 0.0
s.foo = 'bar'
