import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int),
                ("c", ctypes.c_char_p),
                ("d", ctypes.c_char * 4)]

assert X.a.offset == 0
assert X.b.offset == 1
assert X.c.offset == 5
assert X.d.offset == 9

assert X.a.size == 1
assert X.b.size == 4
assert X.c.size == ctypes.sizeof(ctypes.c_char_p)
assert X.d.size == 4

assert X.a.type is ctypes.c_char
assert X.b.type is ctypes.c_int
assert X.c.type is ctypes.c_char_p
assert X.d.type is ctypes.c_char * 4

assert X.a.__name__ == "a"
assert X.b.__name__ == "b"
assert X.c.__name__ == "c
