import ctypes
# Test ctypes.CFUNCTYPE for void return values with optional argument
from ctypes import *

def func(*args):
    pass

FUNC = CFUNCTYPE(None)(func)
FUNC(None)

try:
    FUNC(1)
except TypeError:
    pass
else:
    print("should have raised TypeError")

try:
    FUNC(1,2)
except TypeError:
    pass
else:
    print("should have raised TypeError")

from ctypes import *

def func(*args):
    print(args)

FUNC = CFUNCTYPE(None, c_int, c_int)(func)
FUNC(1,2)
FUNC(1,2,3)

try:
    FUNC(1)
except TypeError:
    pass
else:
    print("should have raised TypeError")

from ctypes import *

def func(*args):
    print(args)

FUNC = CFUNCTYPE(None, c_int, c_int, c_int)(func)
