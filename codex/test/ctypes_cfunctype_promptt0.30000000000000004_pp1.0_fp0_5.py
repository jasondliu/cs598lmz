import ctypes
# Test ctypes.CFUNCTYPE
#
# This is a test case for http://bugs.python.org/issue1202.
#
# The problem was that the CFUNCTYPE() constructor did not properly
# initialize the c_functype_cache dictionary.  This caused a crash
# when the CFUNCTYPE() constructor was called recursively from within
# a callback function.

import unittest
