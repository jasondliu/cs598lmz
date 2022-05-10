import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.
#
# The test is based on the following code:
#
#   #include <stdio.h>
#
#   typedef int (*intFunc) ();
#
#   int
#   bridge_int_func(intFunc f)
#   {
#        return f();
#   }
#
#   int fortytwo()
#   {
#        return 42;
#   }
#
#   int main(int argc, char *argv[])
#   {
#        intFunc f = fortytwo;
#        printf("%d\n", bridge_int_func(f));
#        return 0;
#   }
#
# This is compiled into a shared library, and the resulting shared library
# is loaded using ctypes.

import unittest
from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        cdll.LoadLibrary("libc.so.6")
        lib
