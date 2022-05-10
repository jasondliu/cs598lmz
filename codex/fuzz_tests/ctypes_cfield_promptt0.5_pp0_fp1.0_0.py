import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]
assert X.a.offset == 0
assert X.b.offset == ctypes.sizeof(ctypes.c_char)
# Test ctypes.CField.from_address
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]
x = X()
f = ctypes.Field.from_address(ctypes.addressof(x), ctypes.c_int)
assert f.offset == ctypes.sizeof(ctypes.c_char)
assert f.size == ctypes.sizeof(ctypes.c_int)
# Test ctypes.Field.from_param
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_int)]
x = X()
f = ctypes.Field.from_
