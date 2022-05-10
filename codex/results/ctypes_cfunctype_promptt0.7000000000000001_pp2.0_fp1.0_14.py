import ctypes
# Test ctypes.CFUNCTYPE.
import _ctypes_test

# Test that _ctypes_test.func accepts pointers and ints.
assert _ctypes_test.func(ctypes.c_int(123), ctypes.c_int(456)) == 123 + 456

# Test that _ctypes_test.func does not accept ctypes.c_char().
py.test.raises(TypeError, _ctypes_test.func, ctypes.c_char(b'A'), ctypes.c_int(456))

# Test that _ctypes_test.func does not accept bytes/unicode.
py.test.raises(TypeError, _ctypes_test.func, b'A', ctypes.c_int(456))
py.test.raises(TypeError, _ctypes_test.func, u'A', ctypes.c_int(456))

# Test that _ctypes_test.func does not accept tuples.
py.test.raises(TypeError, _ctypes_test.func, (1, 2, 3), ctypes.c_int(
