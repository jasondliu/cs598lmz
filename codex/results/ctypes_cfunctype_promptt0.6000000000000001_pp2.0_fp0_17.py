import ctypes
# Test ctypes.CFUNCTYPE
#
# This test tests the following cases
#
# - ctypes function returning a function pointer.
# - creating a function pointer from a function.
# - creating a function pointer from a ctypes function.
# - creating a function pointer from a ctypes function pointer.
# - creating a function pointer from a function pointer.
# - calling a function pointer.
#
# This test also tests the following cases
# - ctypes function returning a struct containing a function pointer.
# - creating a struct containing a function pointer from a function.
# - creating a struct containing a function pointer from a ctypes function.
# - creating a struct containing a function pointer from a ctypes function pointer.
# - creating a struct containing a function pointer from a function pointer.
# - calling a struct containing a function pointer.
#
# Other tests that test ctypes.CFUNCTYPE
# - test_keepalive.py
# - test_paramflags.py

import unittest
from ctypes import *
import _ctypes_test

class TestCFUNCTYPE(unittest.TestCase):

    def test_
