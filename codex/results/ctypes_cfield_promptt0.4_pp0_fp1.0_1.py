import ctypes
# Test ctypes.CField

# Test CField.from_address
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int),
                ("d", ctypes.c_int),
                ("e", ctypes.c_int),
                ("f", ctypes.c_int),
                ("g", ctypes.c_int),
                ("h", ctypes.c_int),
                ("i", ctypes.c_int),
                ("j", ctypes.c_int),
                ("k", ctypes.c_int)]

x = X()
x.a = 1
x.b = 2
x.c = 3
x.d = 4
x.e = 5
x.f = 6
x.g = 7
x.h = 8
x.i = 9
x.j = 10
x.k = 11

f = ctypes.CField.from_address(ctypes.addressof(x), ctypes.c
