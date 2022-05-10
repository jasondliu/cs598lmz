import ctypes
# Test ctypes.CFUNCTYPE
cbifunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x * 3)
assert cbifunc(3) == 9
# Test ctypes.WINFUNCTYPE
cbifunc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x * 3)
assert cbifunc(3) == 9

# Test callbacks
import _ctypes
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(
        lambda x: ctypes.pythonapi.PyErr_WarnEx(3,
                                                b"Warning message",
                                                42) or x * 3)

assert f(3) == 9
try:
    f(0)
except TypeError:
    pass
else:
    raise AssertionError("Expected TypeError")

f = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int)(
        lambda x:
