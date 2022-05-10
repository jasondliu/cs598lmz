import ctypes
# Test ctypes.CField
class BAR(ctypes.Structure):
    _fields_ = [("a", ctypes.c_float),
                ("b", ctypes.c_float),
                ("c", ctypes.c_float),
                ("d", ctypes.c_float),
                ("e", ctypes.c_float)]

class FOO(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_float),
                ("e", BAR),
                ("f", ctypes.c_int)]

foo = FOO()
foo.a = 1
foo.b = 2
foo.c = 3
foo.d = 4.0
foo.e.a = 5.0
foo.e.b = 6.0
foo.e.c = 7.0
foo.e.d = 8.0
foo.e.e = 9.0
foo.f = 10

print(foo.a)
