import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [
        ('x', ctypes.c_int),
        ('s', ctypes.c_char_p),
        ('u', ctypes.c_char_p),
        ('v', ctypes.c_char_p),
        ('y', ctypes.c_int),
    ]

s = S()
s.x = 1
s.s = "hello"
s.u = "world"
s.v = "world"
s.y = 2

print s.s == s.v
</code>

