import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.  It should print:
#
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#
# and then exit.

import sys
import ctypes
from ctypes import *

# This is the function we'll call from Python.
def func(a, b, c, d):
    print a, b, c, d

# This is the function we'll call from C.
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, c_int, c_int)

# This is the C code.
CODE = """
#include <stdio.h>

int callfunc(int a, int b, int c, int d, int (*func)(int, int, int, int))
{
    return func
