import ctypes
# Test ctypes.CFUNCTYPE().
#
# Implemented by Thomas Heller 2001-07-19.

from ctypes import *
from ctypes.test.test_pickling import container
from ctypes.util import find_library
from ctypes.test.test_pickling import C; C
from openpyxl.styles import Alignment; Alignment
from cStringIO import StringIO; StringIO


##
# Create C functions
##

dll = CDLL(find_library("c"))
strchr = dll.strchr
strchr.argtypes = c_char_p, c_char
strchr.restype = c_char_p

##
# function pointers as arguments, return values.
##

chk = CFUNCTYPE(c_int, c_void_p)(
    lambda p: 0
    )

def callback(result, func, args):
    global last_args
    last_args = args
##
# Test
##

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1
