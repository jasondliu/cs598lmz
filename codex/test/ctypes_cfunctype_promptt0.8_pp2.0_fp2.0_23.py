import ctypes
# Test ctypes.CFUNCTYPE(), and make sure ctypes.cast() can be applied to functions.

from ctypes import *

int_array10 = c_int * 10

