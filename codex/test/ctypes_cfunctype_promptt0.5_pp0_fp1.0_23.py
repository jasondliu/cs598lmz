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
