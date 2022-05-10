import types
# Test types.FunctionType
import sys
try:
    import win32api
except ImportError:
    pass

import unittest

from test import support

class TypesTests(unittest.TestCase):

    def test_types(self):
        self.assertIsInstance(int, type)
        self.assertIsInstance(type(None), type)
        self.assertIsInstance(object, type)
        self.assertIsInstance(int, object)
        self.assertIsInstance(type(Ellipsis), type)
        self.assertEqual(type(Ellipsis), type)
        self.assertIsInstance(type(type), type)
        self.assertEqual(type(type), type)
        self.assertIsInstance(type, type)
        self.assertIsInstance(object, type)
        self.assertIsInstance(object, object)

        self.assertIsInstance(True, bool)
        self.assertIs(type(True), bool)

        self.assertIsInstance(False, bool)
        self.assertIs(type(False), bool)

        self.
