import ctypes
# Test ctypes.CFUNCTYPE.

import unittest
from test import test_support

# On Windows, ctypes.c_int is an alias for ctypes.c_long.
# This is for backward compatibility with older code.
# We don't want the tests to behave differently on Windows,
# therefore we use c_int here.
c_int = ctypes.c_int

# The rest of the file is taken from Lib/ctypes/test/test_cfunctype.py
# with the following modifications:
# - the tests are now subclasses of unittest.TestCase
# - test_case_1 is skipped, it is invalid
#     def test_case_1(self):
#         # The only parameter is a pointer to an integer.
#         # We must not use the '&' operator here, because
#         # Python integers are not supported by CFUNCTYPE,
#         # the correct way is to pass a pointer to an integer
#         # (here: by using pointer())
#         getint = CFUNCTYPE(c_int, POINTER(c_int))(get
