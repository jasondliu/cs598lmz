import ctypes

class S(ctypes.Structure):
    x = 1.0
    _fields_ = [("foo", ctypes.c_double),
                ("byte1", ctypes.c_byte),
                ("bar", ctypes.POINTER(ctypes.c_double)),
                ("byte2", ctypes.c_byte),
                ]

s = S()
s.foo = 42.0
s.bar = ctypes.pointer(ctypes.c_double(1.0))

