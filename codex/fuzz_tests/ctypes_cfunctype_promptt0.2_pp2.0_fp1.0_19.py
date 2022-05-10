import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.  It is a bit more complex than the
# other tests, because it uses a function pointer as a parameter to a
# function.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        # This test is a bit more complex than the others, because it
        # uses a function pointer as a parameter to a function.
        #
        # The function we are going to call is 'qsort', which is
        # declared in stdlib.h as:
        #
        #   void qsort(void *base, size_t nmemb, size_t size,
        #              int(*compar)(const void *, const void *));
        #
        # The 'compar' parameter is a function pointer, which is used
        # to compare two elements.  The function must return an integer
        # less than, equal to, or greater than zero if the first
        # argument is considered to be respectively less than, equal to,

