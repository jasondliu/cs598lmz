import ctypes
# Test ctypes.CField
f = ctypes.CField(ctypes.c_int, 'foo', 'i = 12345')
assert f.offset == 0, f.offset
assert f.bitsize == 0, f.bitsize
assert f.type == ctypes.c_int, f.type
assert f.size is None, f.size

f = ctypes.CField(ctypes.c_float, 'baz', '3', 30)
assert f.offset == 30, f.offset
assert f.bitsize == 0, f.bitsize
assert f.type == ctypes.c_float, f.type
assert f.size is None, f.size

f = ctypes.CField(ctypes.c_short, 'bar', '2', 15, 16)
assert f.offset == 15, f.offset
assert f.bitsize == 16, f.bitsize
assert f.type == ctypes.c_short, f.type
assert f.size is None, f.size

f = ctypes.CField(ctypes.c_byte, 'bzr', '1',
