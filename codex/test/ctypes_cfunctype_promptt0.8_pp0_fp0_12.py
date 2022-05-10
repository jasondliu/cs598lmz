import ctypes
# Test ctypes.CFUNCTYPE.

from ctypes import *
import unittest

try:
    c_uint128
except NameError:
    c_uint128 = c_uint64

