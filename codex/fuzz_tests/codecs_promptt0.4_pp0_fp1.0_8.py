import codecs
# Test codecs.register_error()

from test import test_support
import unittest

class CodecsTest(unittest.TestCase):

    def test_register_error(self):
        # Test codecs.register_error()
        self.assertRaises(TypeError, codecs.register_error)
        self.assertRaises(TypeError, codecs.register_error, None)
        self.assertRaises(TypeError, codecs.register_error, "replace", None)
        self.assertRaises(TypeError, codecs.register_error, "replace", lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, "replace", lambda x, y: x)
        self.assertRaises(TypeError, codecs.register_error, "replace", lambda x, y, z: x)
        self.assertRaises(LookupError, codecs.register_error, "__spam__")
        self.assertRaises(LookupError, codecs.register_error, "replace", "__spam__")
        self.assertRaises
