import ctypes
# Test ctypes.CFUNCTYPE
#
# This file is part of the llvm-py project
# https://github.com/llvm-mirror/llvm-py
#
# Most of this code comes from the ctypes documentation:
# http://docs.python.org/2/library/ctypes.html
#
# The license of this documentation is in the public domain.
from __future__ import print_function

import sys

from ctypes import CFUNCTYPE, c_int, c_long
from ctypes import pythonapi, py_object

################################################################
# Callback function types

# C: int function(int)
CALLBACK_TYPE_0 = CFUNCTYPE(c_int, c_int)

# C: int function(int, int)
CALLBACK_TYPE_1 = CFUNCTYPE(c_int, c_int, c_int)

# C: int function(int, int, int)
CALLBACK_TYPE_2 = CFUNCTYPE(c_int, c_int, c_int, c_int)

# C
