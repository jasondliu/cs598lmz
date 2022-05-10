import ctypes
# Test ctypes.CField
class CFoo(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_int)]

assert CFoo._fields_ == [("bar", ctypes.c_int)]
assert CFoo.bar == ctypes.c_int

# Test ctypes.CField with offset
class CFoo(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_int, 5)]

assert CFoo._fields_ == [("bar", ctypes.c_int, 5)]
assert CFoo.bar == ctypes.c_int
assert CFoo.bar.offset == 5

# Test ctypes.CField with offset and size
class CFoo(ctypes.Structure):
    _fields_ = [("bar", ctypes.c_int, 5, 4)]

assert CFoo._fields_ == [("bar", ctypes.c_int, 5, 4)]
assert CFoo.bar == ctypes.c_int
assert CFoo.bar.offset == 5
assert CFoo.bar.size == 4

# Test ctypes.
