import ctypes
# Test ctypes.CField instance
import ctypes.test.test_descr
ctypes.test.test_descr.test_CField()

# Test ctypes.Field instance
f = ctypes.Field(ctypes.c_char.from_address(ctypes.addressof(ctypes.c_int())))
assert f.offset == 0
assert f.size == 1
assert f.name == 'c_char'
assert f.ctype == ctypes.c_char

# Test ctypes.Array.
a = ctypes.Array(ctypes.c_int, (1, 2, 3))
assert len(a) == 3
assert a._length_ == 3
assert a[0] == 1
assert a[1] == 2
assert a[2] == 3

assert a[0:1] == a[:1] == a[0:1:1] == a[0:2:1] == (1,)
assert a[1:2] == a[1:3] == a[1:4] == (2,)
assert a[2:3] == a[2:
