import ctypes
# Test ctypes.CField
assert ctypes.CField == ctypes.Field

# Test ctypes.CField.from_address()
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

s = S()

f = ctypes.CField.from_address(id(s), S, "a")
assert f.offset == 0
assert f.type == ctypes.c_int

f = ctypes.CField.from_address(id(s), S, "b")
assert f.offset == ctypes.sizeof(ctypes.c_int)
assert f.type == ctypes.c_int

# Test ctypes.CField.from_buffer()
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

s = S()

f = ctypes.CField.from_buffer(s, S, "a")
assert f.offset == 0
assert f.type ==
