import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_short),
                ("c", ctypes.c_int),
                ("d", ctypes.c_long),
                ("e", ctypes.c_longlong),
                ("f", ctypes.c_float),
                ("g", ctypes.c_double),
                ("h", ctypes.c_char_p),
                ("i", ctypes.c_void_p),
                ("j", ctypes.c_char * 10),
                ("k", ctypes.c_char * 4 * 3),
                ("l", ctypes.c_int * 2 * 3 * 4),
                ("m", ctypes.c_char * 10 * 2 * 3 * 4)]

print(X.a.offset)
print(X.b.offset)
print(X.c.offset)
print(X.d.offset)
print(X.e.offset)
print(X.f.offset)
print(X
