import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test
cfunc = _ctypes_test.get_cfunc_float_float()
assert ctypes.CFUNCTYPE(ctypes.c_float)(cfunc)(3.0) == 3.0
assert ctypes.CFUNCTYPE(ctypes.c_float)(cfunc)(4.0) == 4.0

# Test bools
import _ctypes_test
assert _ctypes_test.get_true() is True
assert _ctypes_test.get_false() is False

# Test PyCapsule
import _ctypes_test
assert _ctypes_test.get_capsule() == (1, 2, "str", u"unicode", 0.5)

# Test NULL pointer
import _ctypes_test
assert _ctypes_test.get_nullptr() is None

# Test raising of gc error when doing a callback on a freed ptr
import _ctypes_test
addr = _ctypes_test.get_ptr_to_free()
f = _ctypes_test.make_cb(addr)
