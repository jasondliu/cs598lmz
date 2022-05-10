import ctypes
# Test ctypes.CFieldError exception. -*- Mode: Python -*-
#
# Tests how things behave when you try to create a basic Python type with
# ctypes, e.g. int.

import unittest
import doctest

from test.support import import_module

ctypes = import_module("ctypes")

class ValueTestCase(unittest.TestCase):
    def test_value(self):
        # Creating an int should not raise an exception, instead
        # ctypes should return None.
        try:
            ctypes.c_int()
        except ctypes.ArgumentError:
            pass
        else:
            raise AssertionError("Expected ctypes.ArgumentError")

def test_main():
    return unittest.TextTestRunner().run(suite)

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(ValueTestCase))
suite.addTest(doctest.DocTestSuite(ctypes.__name__))

if __name__ == '__main__':

