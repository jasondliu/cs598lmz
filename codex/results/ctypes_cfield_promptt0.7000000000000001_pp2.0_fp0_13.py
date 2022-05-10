import ctypes
# Test ctypes.CField from ctypes.test.test_fields
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_double),
                ("b", ctypes.c_double),
                ("c", ctypes.c_double),
                ("d", ctypes.c_double),
                ("e", ctypes.c_double),
                ("f", ctypes.c_double)]
    _pack_ = 4

class Y(ctypes.Structure):
    _fields_ = [("d", ctypes.c_int),
                ("b", ctypes.c_int),
                ("f", ctypes.c_int),
                ("a", ctypes.c_int),
                ("e", ctypes.c_int),
                ("c", ctypes.c_int)]
    _pack_ = 4

def check(x, y):
    for i in range(len(x._fields_)):
        a = x._fields_[i][0]
        b = y._fields_[i][0]
        assert a == b, (
