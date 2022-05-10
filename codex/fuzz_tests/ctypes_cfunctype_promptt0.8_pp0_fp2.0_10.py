import ctypes
# Test ctypes.CFUNCTYPE works correctly
import ctypes.util

import _ctypes_test

libm = ctypes.CDLL(ctypes.util.find_library("m"))

# This worked in 2.5, but fails in 2.6:
#
#   TypeError: don't know how to convert parameter #0
libm.sin.argtypes = ctypes.c_double,

## This should work, too.
#libm.sin.restype = ctypes.c_double

# If the next line is commented in, the atexit handler crashes
# when the program is finished.  This is a different issue from
# issue3691: the crash happens in a module.  So I am opening
# a new issue.
#
#import sys
#sys.exit()

d = ctypes.c_double(1.23)
r = libm.sin(d)
print(r)
