import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a copy of the example in the python docs
#
# https://docs.python.org/2/library/ctypes.html#callback-functions

# WINFUNCTYPE(returns, args)

import ctypes

STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
  _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class SMALL_RECT(ctypes.Structure):
  _fields_ = [("Left", ctypes.c_short), ("Top", ctypes.c_short),
      ("Right", ctypes.c_short), ("Bottom", ctypes.c_short)]

