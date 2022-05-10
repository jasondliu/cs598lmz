import ctypes
# Test ctypes.CFUNCTYPE with a non-integer return value.
import ctypes.util

funcp = ctypes.CFUNCTYPE(ctypes.py_object)

dll = ctypes.CDLL(ctypes.util.find_library('c'))

f = funcp(('pow', dll))
assert f(3, 2) == 9
f.restype = ctypes.c_long
assert f(3, 2) == 9
f.restype = ctypes.c_double
assert f(3, 2) == 9.0
