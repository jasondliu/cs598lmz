import ctypes
# Test ctypes.CFUNCTYPE(), ctypes.pointer() and ctypes.cast()
#

from ctypes import *


##PYB11_begin_exceptions
class MyError(Exception):
    pass
##PYB11_end_exceptions

import sys

##PYB11_begin_preamble
