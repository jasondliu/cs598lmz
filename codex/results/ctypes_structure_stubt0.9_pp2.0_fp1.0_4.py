import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_char),
                ("y", ctypes.c_char),
                ("z", ctypes.c_int),
                ("w", ctypes.c_char),
                ]


s = S()
ctypes.memset(ctypes.addressof(s), 0x12, ctypes.sizeof(s))
print ctypes.sizeof(s)
print s.x, s.y, s.z, s.w
