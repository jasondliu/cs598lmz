import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_float in the presence of a Python
# subtype of c_float.

import ctypes
from ctypes import *

class Sub_float(c_float):
    pass

