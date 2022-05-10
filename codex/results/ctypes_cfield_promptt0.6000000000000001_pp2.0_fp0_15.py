import ctypes
# Test ctypes.CField()
i = ctypes.CField(ctypes.c_int)
assert i.size == ctypes.sizeof(ctypes.c_int)
assert i.alignment == ctypes.alignment(ctypes.c_int)

# Test ctypes.CField.from_address()
from_addr = ctypes.CField.from_address(ctypes.addressof(i))
assert from_addr == i

# Test ctypes.CStruct()
from ctypes import *
class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]
p = Point(1, 2)
assert p.x == 1
assert p.y == 2

# Test ctypes.CStruct.from_buffer()
from_buf = Point.from_buffer(p)
assert from_buf == p

# Test ctypes.CStruct.from_buffer_copy()
from_buf_cpy = Point.from_buffer_copy(p)
assert from_buf_cpy == p

# Test ctypes.CStruct.
