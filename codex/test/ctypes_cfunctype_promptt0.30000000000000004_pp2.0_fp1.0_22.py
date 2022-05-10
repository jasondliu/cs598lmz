import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

def func(*args):
    return args

FUNC = CFUNCTYPE(c_int, c_int, c_int, c_int)

f = FUNC(func)

