import ctypes
# Test ctypes.CFUNCTYPE
#
# This test case is from
# http://bytes.com/topic/python/answers/624976-ctypes-callback-function
#
# This is a test for ctypes.CFUNCTYPE.  The goal is to be able to pass
# a callback function to a C library for a callback.  The callback
# will be called by the C library and passed a pointer to a struct.
#
# The struct contains a field that is a pointer to a function that is
# part of the struct.  The function is called by the C library.
#
# This is the struct that is passed to the callback function.  It
# contains a pointer to a function.

from ctypes import *

