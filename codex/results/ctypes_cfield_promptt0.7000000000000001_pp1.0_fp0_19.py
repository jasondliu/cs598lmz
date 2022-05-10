import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]
    class b(ctypes.Union):
        _fields_ = [('c', ctypes.c_int),
                    ('d', ctypes.c_float)]

# Test ctypes.CField
class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_float),
                ('c', ctypes.c_double),
                ('d', ctypes.c_byte)]

# Test ctypes.CField
class E(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_float),
                ('c', ctypes.c_double),
                ('d', ctypes.c_byte),
                ('e', ctypes.c_char)]

# Test ctypes.CField
class F(ctypes.Structure):
    _fields_ = [('a', ctypes.c_
