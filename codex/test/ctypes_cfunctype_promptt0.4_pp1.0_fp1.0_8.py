import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a simple test of ctypes.CFUNCTYPE.

import ctypes
from ctypes import *

################################################################

# Some simple callback functions

# A callback function taking no arguments and returning an int
CALLBACKFUNC = CFUNCTYPE(c_int)

def callbackfunc():
    return 42

c_callbackfunc = CALLBACKFUNC(callbackfunc)

# A callback function taking an int argument and returning an int
CALLBACKFUNCINT = CFUNCTYPE(c_int, c_int)

def callbackfuncint(value):
    return value + 1

c_callbackfuncint = CALLBACKFUNCINT(callbackfuncint)

# A callback function taking a float argument and returning a float
CALLBACKFUNCFLOAT = CFUNCTYPE(c_float, c_float)

def callbackfuncf(value):
    return value + 1.0

c_callbackfuncf = CALLBACKFUNCFLOAT(callbackfuncf)

# A callback function taking an int argument and returning a pointer

