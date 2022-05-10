import ctypes
# Test ctypes.CField()


class X1(ctypes.Structure):
    _fields_ = [
        ('f1', ctypes.c_int, 1),
        ('f2', ctypes.c_int, 2),
        ('f3', ctypes.c_int, 3),
        ('f4', ctypes.c_int, 4),
        ('f5', ctypes.c_int, 5),
        ('f6', ctypes.c_int, 6)
    ]


class X2(ctypes.Structure):
    _fields_ = [
        ('f1', ctypes.c_int, 1),
        ('reserved', ctypes.c_int, 3),
        ('f5', ctypes.c_int, 5),
        ('reserved2', ctypes.c_int, 4),
        ('f10', ctypes.c_int, 10),
    ]


class X3(X2):
    _fields_ = X2._fields_ + [
        ('f20', ctypes.c_int, 20),
    ]


class X4
