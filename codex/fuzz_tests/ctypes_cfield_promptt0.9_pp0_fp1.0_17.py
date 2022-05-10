import ctypes
# Test ctypes.CField


class A(ctypes._CData):
    _fields_ = [("a", ctypes.c_int)]


class B(ctypes._CData):
    _fields_ = [("b", ctypes.c_int8)]


class C(ctypes._CData):
    _fields_ = [("a", A), ("b", B)]


class D(ctypes._CData):
    # This stucture has gaps, these will be filled with padding
    _fields_ = [("a", ctypes.c_int8),
                ("b", ctypes.c_int32),
                ("c", ctypes.c_int16)]

# See if the offset is correctly calculated


class E(ctypes._CData):
    _fields_ = [("a", ctypes.c_char * 3)]
    _anonymous_ = ("a",)


class F(ctypes._CData):
    _fields_ = [("b", ctypes.c_int8),
                ("c", ctypes.c_char * 3),
                ("d", c
