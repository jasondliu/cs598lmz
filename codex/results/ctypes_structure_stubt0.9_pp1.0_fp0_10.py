import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong

    __slots__ = ('y',)
    _fields_ = [
        ('x', ctypes.c_longlong),
        ('y', ctypes.c_int),
        ('z', ctypes.c_int),              # this is a padding field when compiled with -O0 but not with -O1
    ]

s = S()
s.x = 42
s.y = 23
s.z = 24                               # only with -O0

print(s.x, s.y, s.z)
</code>

