import ctypes
# Test ctypes.CFUNCTYPE with byref(c_float) and byref(c_double).
# The test passes if no segfault or assertion failure occurs.

libm = ctypes.CDLL(ctypes.util.find_library("m"))

f = ctypes.CFUNCTYPE(None, ctypes.byref(ctypes.c_float))
d = ctypes.CFUNCTYPE(None, ctypes.byref(ctypes.c_double))

f(libm.fabs)
d(libm.fabs)

f(libm.sin)
d(libm.sin)

f(libm.cos)
d(libm.cos)

f(libm.tan)
d(libm.tan)

f(libm.asin)
d(libm.asin)

f(libm.acos)
d(libm.acos)

f(libm.atan)
d(libm.atan)

f(libm.sinh)
d(libm.sinh)

f(
