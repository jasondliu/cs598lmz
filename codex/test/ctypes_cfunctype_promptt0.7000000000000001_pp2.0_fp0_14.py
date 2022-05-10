import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is different from all other tests in this directory:
# we don't write a Python program in a .py file, and we don't call
# the C compiler.  Instead, we build a DLL on-the-fly in memory with
# ctypes, and then run it; if it works, it prints "success".

from ctypes import *

NULL = None
FALSE = 0
TRUE = 1

# /Oi is needed to generate a function prototype for printf()
# otherwise the code is not valid C89.
