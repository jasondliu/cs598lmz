import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p()

class S2(ctypes.Structure):
    _fields_ = [('a', ctypes.c_long),
                ('b', ctypes.c_char_p)]

class S3(ctypes.Structure):
    pass

class S4(ctypes.Structure):
    pass

S4._fields_ = [('a', ctypes.c_long),
               ('b', ctypes.c_char_p)]

class S5(ctypes.Structure):
    pass

S5._fields_ = [('a', ctypes.c_long),
               ('b', ctypes.c_char_p)]
S5._fields_.append(('c', ctypes.c_char_p))

class S6(ctypes.Structure):
    _fields_ = [('a', ctypes.c_long),
                ('b', ctypes.c_char_p),
                ('c', ctypes.c_char_p)]

