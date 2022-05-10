import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

libm = ctypes.CDLL(ctypes.util.find_library("m"))

# Test returning a double
cos = libm.cos
cos.restype = ctypes.c_double
print cos(1.23)

# Test returning void
libc = ctypes.CDLL(ctypes.util.find_library("c"))
puts = libc.puts
puts.restype = None
puts("Hello World")

# Test passing a double
sin = libm.sin
sin.argtypes = ctypes.c_double,
sin.restype = ctypes.c_double
print sin(0.123)
