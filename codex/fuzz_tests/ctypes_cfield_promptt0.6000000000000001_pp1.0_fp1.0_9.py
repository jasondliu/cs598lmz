import ctypes
# Test ctypes.CField()

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ctypes.CField("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ctypes.CField("d", ctypes.c_int),
        ("e", ctypes.c_int),
    ]

obj = X()
obj.a, obj.b, obj.c, obj.d, obj.e = 1, 2, 3, 4, 5
print(obj.a, obj.b, obj.c, obj.d, obj.e)
print(X.b, X.d)

# Test ctypes.CField() with a string

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ctypes.CField("b", "c_int"),
        ("c", ctypes.c_int),
        ctypes.CField("d", "c_int"),
        ("e
