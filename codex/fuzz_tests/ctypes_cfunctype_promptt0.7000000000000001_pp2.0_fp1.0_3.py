import ctypes
# Test ctypes.CFUNCTYPE
#
# The following code is intended to be compiled using a C compiler,
# and the resulting object file then loaded using ctypes.cdll.LoadLibrary.
#
#   void call_func(void (*func)(int, long, int))
#   {
#       func(1, 2L, 3);
#   }
#
#   void call_func_callback(void (*func)(void))
#   {
#       func();
#   }
#
#   int call_func_callback_retval(int (*func)(void))
#   {
#       return func();
#   }

import sys
import unittest
from test import support

if sys.platform == 'win32':
    from ctypes import wintypes
else:
    wintypes = None

@unittest.skipUnless(sys.platform == 'win32', 'Windows-specific test')
class CFuncPtrTestCase(unittest.TestCase):

    def setUp(self):
        self.dll = ctypes.cdll.LoadLibrary(support.TESTFN)


