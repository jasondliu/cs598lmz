import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int)) as callback
# type.

import unittest
import ctypes
from ctypes import util

class CallbackTest(unittest.TestCase):
    def callback(self, pointer):
        self.got_pointer = pointer

    def test_callback(self):
        function = ctypes.CFUNCTYPE(None, ctypes.POINTER(ctypes.c_int))(self.callback)
        self.got_pointer = None
        function(42)
        self.assertIsNotNone(self.got_pointer)
        self.assertEqual(self.got_pointer.contents.value, 42)

    def test_errcheck(self):
        def errcheck(result, func, arguments):
            self.assertEqual(result, 42)
            self.assertEqual(len(arguments), 2)
            self.assertIsInstance(arguments[0], ctypes.c_int)
            self.assertIsInstance(arguments[1], ctypes.c_int)
            self
