import ctypes
# Test ctypes.CFUNCTYPE

# This should work in both Python2 and Python3
# However, it will fail in Python3 if you
# use the following flags: -O -OO

# Also, this runs fine on my Linux box with
# Python 2.5.2, but generates a segfault
# on my Mac with Python 2.5.1

import ctypes
import ctypes.util

libc = ctypes.CDLL(ctypes.util.find_library("c"))

#  void qsort(void *base, size_t nel, size_t width,
#             int (*compar)(const void *, const void *));

# The restype and argtypes are just hints to the interpreter.
# It doesn't actually check them.
libc.qsort.restype = None
libc.qsort.argtypes = (ctypes.c_void_p,
                       ctypes.c_size_t,
                       ctypes.c_size_t,
                       ctypes.CFUNCTYPE(ctypes.c_int,
                                        ctypes.c_void_
