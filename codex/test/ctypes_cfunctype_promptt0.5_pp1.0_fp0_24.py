import ctypes
# Test ctypes.CFUNCTYPE
#
# Note: this example is not complete.  You will need to add other
# declarations and callbacks to fully test ctypes.CFUNCTYPE
#
# This example is based on the file callback.c in the Python 2.3.3
# distribution.
#
# Written by: Michael Hudson <mwh@python.net>
#
# $Id: callback.py,v 1.1 2003/12/16 14:22:13 mwh Exp $

from ctypes import *

# This is some dummy external function that takes a callback as
# argument.  It is just here to test ctypes.CFUNCTYPE

#_callback = CFUNCTYPE(c_int, c_int, c_int)
#def callback(arg1, arg2):
#    return arg1 * arg2

#_callback = CFUNCTYPE(c_int, c_int, c_int)
#def callback(arg1, arg2):
#    return arg1 * arg2

