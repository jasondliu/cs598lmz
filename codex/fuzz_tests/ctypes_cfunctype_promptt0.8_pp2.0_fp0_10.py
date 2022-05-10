import ctypes
# Test ctypes.CFUNCTYPE() with restypes which are not ctypes instances.
# http://bugs.python.org/issue17591
#
import unittest, sys


class CFUNCTYPTETest(unittest.TestCase):
    def test_string_restype(self):
        CFUNC = ctypes.CFUNCTYPE(ctypes.c_char_p)
        func = CFUNC(lambda: 'abc')
        self.assertEqual(func(), 'abc')

    def test_integer_restype(self):
        CFUNC = ctypes.CFUNCTYPE(ctypes.c_int)
        func = CFUNC(lambda: 123)
        self.assertEqual(func(), 123)

    def test_non_callable_restype(self):
        CFUNC = ctypes.CFUNCTYPE(123)
        try:
            CFUNC(lambda: None)
        except TypeError as e:
            self.assertIn('Callable', str(e))
        else:
            self.fail('TypeError should have been raised
