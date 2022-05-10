import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_byte),
                ('z', ctypes.c_byte),
                ('w', ctypes.c_byte),
                ('a', ctypes.c_byte),
                ]


class BS(ctypes.Structure):
    x = ctypes.c_int(0)
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_byte),
                ('z', ctypes.c_byte),
                ('w', ctypes.c_byte),
                ('a', ctypes.c_byte),
                ]


with open('foo', 'wb') as f:
    s = S()
    f.write(s)
    f.write(s)

with open('bar', 'wb') as f:
    bs = BS()
    f.write(bs)
    f.write(bs)
