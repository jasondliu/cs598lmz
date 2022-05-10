import ctypes
# Test ctypes.CFUNCTYPE.
def _longjmp(j, val):
    raise ctypes.ArgumentError(val, "This is a test")
jumpy_ptr = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_int)(_longjmp)
try:
    j = ctypes.c_void_p(123)
    jumpy_ptr(j, 1)
except ctypes.ArgumentError as e:
    assert e.args == (1, "This is a test")
