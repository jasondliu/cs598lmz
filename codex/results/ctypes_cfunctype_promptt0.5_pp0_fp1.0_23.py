import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is modified from python/lib/test/test_ctypes.py
#
# The test is skipped on Windows because the function pointer
# is not converted correctly.
#
# The test is skipped on OS X because the function pointer
# is not converted correctly.
#
# The test is skipped on 32-bit Linux because the function pointer
# is not converted correctly.

import os
import sys
import unittest
from test import support

# Skip test if _ctypes module is not available.
support.import_module('_ctypes')

from ctypes import *

if sys.platform == 'win32':
    raise unittest.SkipTest("test skipped on Windows")

if sys.platform == 'darwin':
    raise unittest.SkipTest("test skipped on OS X")

if sys.maxsize == 2**31-1:
    raise unittest.SkipTest("test skipped on 32-bit Linux")

# This test is expected to run on 64-bit Linux only.

def func(a, b):
    return a + b


