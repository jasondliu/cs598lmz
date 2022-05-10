import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_char)]
    _anonymous_ = [('c', ctypes.c_char)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_char),
                ('d', ctypes.c_char)]
    _anonymous_ = [('c', ctypes.CField)]

class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_char),
                ('e', ctypes.c_char)]
    _anonymous_ = [('c', ctypes.CField)]

class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_char),
                ('f', ctypes.c_char)]
    _anonymous_ = [('
