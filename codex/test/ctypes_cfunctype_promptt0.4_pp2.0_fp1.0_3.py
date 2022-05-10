import ctypes
# Test ctypes.CFUNCTYPE()

from ctypes import *

# void func(int)
FUNC = CFUNCTYPE(None, c_int)

